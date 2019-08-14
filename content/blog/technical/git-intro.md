title: Git is Weird
date: 2019-07-27 12:48:41
modified: 2019-07-27 12:48:41
status: draft

You use git branch to list and create branches, but you use git checkout to
*switch* to a branch, unless it's a new branch, in which case it can also be
used to also create the branch if you supply it with the -b option.

So far this isn't actually that bad.  The checkout command is your moving
around command - you can use it to switch to an arbitrary commit, for
example.  The branch command is your branch management command.  The -b
option to the checkout command does add a certain wart to the whole thing -
it would be more intuitive, in my opinion, if the branch command created
*and* switched you to the branch automatically - but so far it's nothing
horrible.

Ah! but you also use git checkout when you want to *revert* a *file*, i.e.
undo the local changes you just made to it.  I understand the underlying
conceptual link between the two use cases, but it's not the normal way I
usually think about these operations.  There is, in fact, a git revert
comand but, surprisingly, it doesn't actually work on files - it's used to
create commits which undo (revert) other commits.  Of course, if you want to
just revert all the local changes in your repo, you can do so with the git
reset command, which also doesn't work on individual files, but which
provides a plethora of options, mostly revolving around whether your changes
are *staged* or not.

Oh yeah, git provides a staging area, which I've personally found of limited
value, especially when you consider how easy it is to amend commits.
