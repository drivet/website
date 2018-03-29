title: Blogging with Emacs and Pelican
date: 2018-03-22 10:06:38
modified: 2018-03-22 10:06:38
status: draft

[Pelican][1] is my blogging engine of choice these days.  Given that
[emacs][2] is often (but not always) my text editor of choice, it made sense
to try and streamline the process of writing blog entries for pelican with
emacs.  What follows is my attempt to document such an endeavor, partly
because I think it might be useful to the (undoubtedly tiny) cross section
of people who use both emacs and pelican, but mostly so that I have
something to refer back to when the need arises.

## Projectile and Version Control

Emacs is already pretty good at editing files, once you manage to find and
load them into buffers. _Projectile_, on the other hand, is an emacs package
for managing the (sometimes very large) collection of files that make up
your _project_ (such as, to pick an example out of thin air, your pelican
blog).  You can peruse the [github page][4] for more information but,
briefly, with projectile you can easily do things like find a file, perform
a grep, or run a compile command, all scoped to the particular project
you're working on.  A good chunk of the advantages of using emacs for
writing pelican entries ultimately stem from using projectile.

Projectile's notion of a "project" is flexible but version controlled repos
(such as those managed by git, mercurial, daarcs or bazaar) are treated as
such by default.  Thus, the first step should be to put your pelican blog
under one of these version control systems.  The usual advantages of a
version control system apply but, more importantly with respect to emacs
integration, you get to use projectile out of the box.

## Using Magit

I chose git as my version control system for my blog.  I'll cop to
preferring the comparably tidy mercurial command line interface to git's
hodge podge of commands and options, but there are actually several reasons
to specifically use git here:

 * Git has much more mindshare than any other version control system, so
   you're more likely to get help when you need it.
 * [Github][10] is a hotbed of developer activity.  This, in itself,
   probably consitutes the single most important to know and use git.
 * Emacs has rather nice git support in the form of magit.

[Magit][5] is a full git front end embedded in emacs. That makes it a
complex piece of software but if you're like me and you try and keep your
repo history nice and linear, then a little bit of magit goes a long way.
The [Getting Started][6] page basically covers 90% of what you need to know.

Everything starts with the magit status buffer, brought up with the
`magit-status` command.  The guide recommends binding this to `C-x g` and
this is what I've done.  From the status buffer, you can see various
sections displaying various pieces of information, among them:

 * Unstaged changes
 * Staged changes
 * Untracked files

Using the status buffer is pretty easy if you stick to the very basics:

 * Pressing `s` next to an unstaged file will stage it.
 * Pressing `u` next to a staged file will unstage it.
 * Staging/unstaging applies to hunks as well.  You can use TAB to expand a
   file to see the hunks.
 * Pressing `c` will bring up the commit buffer.  Just press `c` again to
   start the commit message, and C-c C-c to make the commit.
 * Pressing `P` will bring up the push buffer, Press `p` to actually push
   your changes
 * Pressing `F` will bring up the pull buffer (i.e. to pull and merge in one
   shot).
   
Git is, of course, capable of much, much more than this, and by extension so
is magit, but I don't make use of these features on my pelican repo, so I
haven't bothered to go that far (yet).

## Compiling and Publishing

Projectile lets you easily run a compile command for your project (C-c p c).
You can configure the default command with the
`projectile-project-compilation-cmd` variable, which I've set via a standard
emacs `.dir-local.el` file located at the root of my blog:

    :::elisp
    ((nil . ((projectile-project-compilation-cmd . "make"))))


My default compile command is a simple `make` because pelican can easily
produce a Makefile for your blog out of the box.  Makefiles can seem rather
old school nowadays, but for something as simple as blog compilation, it's a
good fit.

Pelican's auto-generated Makefile is somewhat bloated so in my case I ended
up removing removed the cruft I wasn't using.  The end result looks like
this:

    :::Makefile
    PY=python
    PELICAN?=pelican
    PELICANOPTS=

    BASEDIR=$(CURDIR)
    INPUTDIR=$(BASEDIR)/content
    OUTPUTDIR=$(BASEDIR)/output

    CONFFILE=$(BASEDIR)/pelicanconf.py
    PUBLISHCONF=$(BASEDIR)/publishconf.py

    SSH_HOST=desmondrivet.com
    SSH_USER=dcr
    SSH_TARGET_DIR=/home/dcr/wwwroot/pelican_blog

    html:
	    $(PELICAN) -s $(CONFFILE) $(INPUTDIR) -o $(OUTPUTDIR)

    clean:
	    [ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

    regenerate:
	    $(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

    publish:
	    $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

    rsync: publish
	    rsync -avzhe ssh $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

    serve:
	    cd $(OUTPUTDIR) && $(PY) -m pelican.server


The targets can be summarized as follows:

 * `html` will generate a local copy of your blog.  This is the default
   target, and hence what gets run by projectile by default.
 * `publish` is like `html` except it uses a special publish conf file.
 * `rsync` depends on `publish` and copies over the generated blog to your
   server with SSH
 * `regenerate` is like `html` but keeps running and will regenerate your
   blog upon detecting that something has changed.
 * `serve` will start a local HTTP server so you can see your blog

Projectile lets you edit the compile command before running it, so you can
easily `publish` and `rsync` using this mechanism as well.

## Using Markdown

My blog entries are all written in [Markdown][7], which I edit in emacs
using [Markdown mode][8].  Markdown's basic idea is to take "natural"
markers in pure text and convert them to HTML; a piece of text flanked by
the "*" symbol, for example, will be rendered in bold.  This is an organic
fit for people like me, who like to write in pure text and who tend to use
these kinds of markers in their writing anyway.

Markdown mode provides syntax highlighting and editing capabilities but
since markdown is already pretty easy to write on its own, and my articles
are not overly structured, I haven't actually made much use of the editing
capabilities.  I just write my text out manually.

One major exception would be the management of external content, like
hyperlinks or images.  It's a bit difficult to devise an organic way to fit
these kinds of artifacts into your writing.  In markdown, there are two ways
to do it.  With option 1, you can inline the URL of the external resource
right next to the text with which it's associated, like this:

    [Some text](http://www.example.com)

With option 2, you can use a reference label which has to match up to a URL
later in your article, like this:

    [Some text][label]  
    ...  
    ...  

    [label]: http://www.example.com

I'm using hyperlinks in the above example.  Images have a similar structure,
but the "text" is considered to be the "alternative text" for the image tag,
like this:

    ![Alt text](/img/piano.jpg)
    
or this:

    ![Alt text][label]
    ...  
    ...  

    [label]: /img/piano.jpg

Both options involve some non-trivial syntax, which is not unexpected given
that links and images are not really "natural" textual artifacts.  I do
prefer the reference style because it makes for better flowing text and the
syntax is a bit easier to remember, but it comes at a cost: you have to
think up a label, and you have to put the actual URL somewhere else in your
document.

Markdown mode helps here.  It provides an interactive command,
`markdown-insert-link` (bound to `C-c C-l`) which is a kind of "all-in-one"
interactive function which lets you enter an inline or reference link,
depending on the parameters you provide.  Reference links will be inserted
at your preferred location (controlled by the `markdown-reference-location`
variable, which I've set to `end`, i.e. the end of my document).

### Automatic Reference Labels

This works, as far as it goes, but it's not quite as convenient as it could
be.  I generally don't try to attach any semantic meaning to my link labels;
my usual approach is to simply use an ever increasing series of numbers.
This lends itself well to automation; my next label is always just the next
number after the previous one.

With some shameless pilfery from [Emacs Wiki][9], I managed to cobble
together some functions to allow me to easily add referenced links and
images, incrementing the label as you add more.  This is my markdown.el
file:


    :::elisp
    (defun my-markdown-insert-reference-image-dwim ()
     "Insert a reference image of the form ![text][label] at point.
    If there is an active region, the text in the region will be used
    as the alt text.  If the point is at a word, it will be used as
    the alt text.  Otherwise, the alt text will be read from the
    minibuffer.  The ref label will be read from the minibuffer in
    both cases, with completion from the set of currently defined
    references.  To create an implicit reference link, press RET to
    accept the default, an empty label.  If the entered referenced
    label is not defined, additionally prompt for the URL
    and (optional) title.  The reference definition is placed at the
    location determined by `markdown-reference-location'."
      (interactive)
      (my-markdown-insert-reference-dwim 't))

    (defun my-markdown-insert-reference-link-dwim ()
     "Insert a reference link of the form [text][label] at point.
    If there is an active region, the text in the region will be used
    as the link text.  If the point is at a word, it will be used as
    the link text.  Otherwise, the link text will be read from the
    minibuffer.  The link label will be read from the minibuffer in
    both cases, with completion from the set of currently defined
    references.  To create an implicit reference link, press RET to
    accept the default, an empty label.  If the entered referenced
    label is not defined, additionally prompt for the URL
    and (optional) title.  The reference definition is placed at the
    location determined by `markdown-reference-location'."
      (interactive)
      (my-markdown-insert-reference-dwim 'nil))

    (defun my-markdown-insert-reference-dwim (image-p)
      (let* ((defined-labels (markdown-get-defined-references))
             (bounds (or (and (markdown-use-region-p)
                              (cons (region-beginning) (region-end)))
                         (markdown-bounds-of-thing-at-point 'word)))
             (text (if bounds
                       (buffer-substring (car bounds) (cdr bounds))
                     (read-string "Text: ")))
             (label (completing-read
                     "Label (default is incremented numerical label): " defined-labels
                     nil nil nil 'markdown-reference-label-history 
                     (next-markdown-label defined-labels)))
             (ref (markdown-reference-definition
                   (concat "[" (if (> (length label) 0) label text) "]")))
             (url (unless ref (read-string "URL: ")))
             (title (when (> (length url) 0)
                      (read-string "Title (optional): "))))
        (when bounds (delete-region (car bounds) (cdr bounds)))
        (if image-p
            (markdown-insert-reference-image text label url title)
          (markdown-insert-reference-link text label url title))))

    (defun next-markdown-label(reflabels)
      (number-to-string (+ 1 (max-list (mapcar 'string-to-number
                            (remove-if-not 'string-integer-p reflabels))))))

    (defun max-list(list)
      (if (not list) 
          0
        (max (car list) (max-list (cdr list)))))

    (defun string-integer-p (string)
       (if (string-match "\\`[-+]?[0-9]+\\'" string)
           t
         nil))

    (defun my-markdown-mode-keys ()
      "Modify keymaps used by `markdown-mode'."
      (local-set-key (kbd "C-c C-a r") 'my-markdown-insert-reference-link-dwim)
      (local-set-key (kbd "C-c C-i r") 'my-markdown-insert-reference-image-dwim))
    (add-hook 'markdown-mode-hook 'my-markdown-mode-keys)

    (setq markdown-reference-location 'end)
    (setq markdown-font-lock-support-mode nil)




## Creating and Finding your Drafts

## Updating Timestamps


[1]: https://blog.getpelican.com

[2]: https://www.gnu.org/software/emacs/

[3]: https://git-scm.com/

[4]: https://github.com/bbatsov/projectile

[5]: https://magit.vc/manual/magit.html

[6]: https://magit.vc/manual/magit.html#Getting-Started

[7]: https://daringfireball.net/projects/markdown/

[8]: https://jblevins.org/projects/markdown-mode/

[9]: https://www.emacswiki.org/

[10]: https://github.com/
