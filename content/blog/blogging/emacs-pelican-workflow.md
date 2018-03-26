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
(such as git, mercurial, daarcs and bazaar repos) are treated as such by
default.  Thus, the first step should be to put your pelican blog under one
of these version control system.  The usual advantages of a version control
system apply but, more importantly with respect to emacs integration, you
get to use projectile out of the box.

## Using Magit

I chose git as my version control system for my blog.  For most people this
would require no justification, but I'm not most people.

I'm not trying to start a war, and I'll admit to preferring the comparably
tidy mercurial command line interface to git's hodge podge of commands and
options, but there are actually several reasons to specifically use git
here:

 * git has much more mindshare than any other version control system, so
   you're more likely to get help when you need it.
 * github is a hotbed of developer activity.  This, in itself, probably
   consitutes the single most important to know and use git.
 * emacs has rather nice git support in the form of magit.

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
 * `regenerate` is like `html` but keeps running and will regenrate your
   blog upon detecting that something has changed.
 * `serve` will start a local HTTP server so you can see your blog

Projectile lets you edit the compile command before running it, so you can
easily `publish` and `rsync` using this mechanism as well.

## Using Markdown

My blog entries are all written in [markdown][7], which I edit in emacs
using [markdown mode][8].  Markdown's basic idea is to take "natural"
markers in pure text and convert them to HTML; a piece of text flanked by
the "*" symbol, for example, will be rendered in bold.  This is an organic
fit for people like me, who like to write in pure text and who tend to use
these kinds of markers in their writing anyway.

Markdown mode provides syntax highlighting and editing capabilities but
since markdown is already pretty easy to write on its own, and my articles
are not overly structured, I haven't actually made much use of the editing
capabilities.  I just write my text manually.

One major exception would be external references, like links.  It's a bit
difficult to devise an organic way to fit these kinds of artifacts into your
writing.  In markdown, there are two ways to do it.  With option 1, you can
inline the URL of the referenced external resource right next to the text
you're trying to hyperlink, like this:

    [Some text](http://www.example.com)

With option 2, you can use a reference label which has to match up to a URL
later in your article, like this:

    [Some text][label]  
    ...  
    ...  

    [label]: http://www.example.com

I almost always use the reference style, because I find that it makes my
text flow better.  Markdown mode makes it easy to add a reference style
link.


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
