title: Blogging with Emacs and Pelican
date: 2018-03-17 19:33:10
modified: 2018-03-17 19:33:10
status: draft

[Pelican][1] is my blogging engine of choice these days.  Given that
[emacs][2] is often (but not always) my text editor of choice, it made sense
to try and streamline the process of writing blog entries for pelican with
emacs.  What follows is my attempt to document such an endeavor, partly
because I think it might be useful to the (undoubtedly tiny) cross section
of people who use both emacs and pelican, but mostly so that I have
something to refer back to when the need arises.

## Git and Projectile

The first step is to put your pelican blog under [git][3] control.  If
you're using pelican you're probably already doing this, but just in case
you're not, you should.  The usual advantages of a version control system
(history, file diffs, etc.) apply but, more importantly with respect to
emacs integration, you get to use a package called _projectile_ out of the
box.

Emacs is already pretty good at editing files, once you manage to find and
load them into buffers; projectile, on the other hand, is an emacs package
for managing the (sometimes very large) collection of files that make up
your _project_.  You can peruse the [github page][4] for more information but,
briefly, with projectile you can easily do things like find a file, perform
a grep, or run a compile command, all scoped to the particular project
you're working on.  A good chunk of the advantages of using emacs for
writing pelican entries ultimately stem from using projectile.

Projectile's definition of a "project" is flexible but git repos are
considered such by default which, as mentioned above, is one major reason
you should use it.

## Using Magit

In general, projectile considers several types of versioned controlled repos
(git, mercurial, daarcs and bazaar) to be projects by default.  So why
choose git in particular?

I'm not trying to start a war, and I'll admit to preferring the rather tidy
mercurial command line interface to git's hodge podge of commands and
options, but there actually several reasons to specifically use git here:

 * git has much more mindshare than any other VCS, and so you're more likely
   to get help when you need it.
 * github is a hotbed of developer activity.  This, in itself, probably
   consitutes the single most important to know and use git.
 * emacs has rather nice git support in the form of magit.

[Magit][5] is a full git front end embedded in emacs. That makes it a
complex piece of software but if you're like me and you are the sole
maintainer of your repo, then a little bit of magit goes a long way.  The
[Getting Started][6] chapter basically covers 90% of what you need to know.

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
 * Pressing `F` will bring up the pull buffer (i.e.  to pull and merge in
   one shot).
   
Git is, of course, capable of much, much more than this, but I don't make
use of these features on my pelican repo, so I haven't bothered to figure
out how to do them with magit.

## Compiling and Publishing

## Using Markdown

## Creating and Finding your Drafts

## Updaing Timestamps

[1]: https://blog.getpelican.com

[2]: https://www.gnu.org/software/emacs/

[3]: https://git-scm.com/

[4]: https://github.com/bbatsov/projectile

[5]: https://magit.vc/manual/magit.html

[6]: https://magit.vc/manual/magit.html#Getting-Started
