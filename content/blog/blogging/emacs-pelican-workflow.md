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

## Version Control and Projectile

The first step is to put your pelican blog under version control.  If you're
using pelican you're probably already doing this, but just in case you're
not, you should.  The usual advantages of a version control system (history,
file diffs, etc.) obviously apply but, more importantly with respect to
emacs integration, you get to use projectile out of the box.

Projectile is an emacs package for managing files at the project level.  You
can certainly peruse the github page for more information but, briefly, with
projectile you can easily do things like find a file, perform a grep, or
compile all scoped to the project you're working on.  Basically, most of the
advantages of using emacs for writing pelican entries stem from using
projectile.

Projectile's definition of a "project" is flexible but versioned repos using
git or mercurial are considered projects automatically which, as mentioned,
is one major reason you should do it.



[1]: https://blog.getpelican.com
