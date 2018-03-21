title: Blogging with Emacs and Pelican
date: 2018-03-17 19:33:10
modified: 2018-03-17 19:33:10
status: draft

[Pelican][1] is my blogging engine of choice these days.  Given that emacs
is often (but not always) my text editor of choice, it made sense to try and
streamline the process of writing blog entries for pelican with emacs.  What
follows is my attempt to document such an endeavor, partly because I think
it might be useful to the (undoubtedly tiny) cross section of people who use
both emacs and pelican, but mostly so that I have something to refer back to
when the need arises.

## Git and Projectile

The first step is to put your pelican blog under git control.  If you're
using pelican you're probably already doing this, but just in case you're
not, you should.  The usual advantages of a version control system (history,
file diffs, etc.) apply but, more importantly with respect to emacs
integration, you get to use a package called _projectile_ out of the box.

Emacs is already pretty good at editing files, once you manage to find and
load them into buffers; projectile, on the other hand, is an emacs package
for managing the (sometimes very large) collection of files that make up
your _project_.  You can peruse the github page for more information but,
briefly, with projectile you can easily do things like find a file, perform
a grep, or run a compile command, all within the scope of the particular
project you're working on.  A good chunk of the advantages of using emacs
for writing pelican entries ultimately stem from using projectile and
treating your pelican blog as a project from its perspective.

Projectile's definition of a "project" is flexible but git repos are
considered such by default which, as mentioned above, is one major reason
you should use it.

## Using Magit

In general, projectile considers most types of versioned controlled repos
(git, mercurial, daarcs and bazaar) to be projects by default.  So why
choose git in particular?

I'm not trying to start a war, and I'll admit to preferring the rather tidy
mercurial command line interface to git's hodge podge of commands and
options, but there actually several reasons to use use git here:

 * git has much more mindshare than any other VCS, and so you're more likely
   to get help when you need it.
 * github is a hotbed of developer activity.  In itself, this probably
   consitutes the single most important to know and use git.
 * emacs has rather nice git support in the form of magit.

[1]: https://blog.getpelican.com

