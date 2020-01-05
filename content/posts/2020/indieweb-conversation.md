title: How to Have a Conversation on the IndieWeb
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft


## It's a Web Page!  It's a Web Service!  It's Both!

Publishing content on your site is great and all, but where do the social
networking aspects fit in to all of this?  How does one "share" a status
update, for example?  How does one "reply" to it?  How does one "like" it?
And how does one do all that in a decentralized manner?

The problem becomes more obvious when one realizes that the IndieWeb does
not prescribe the use of any particular blogging software or, indeed, any
particular technology at all (other than the standard machinery of the web,
like HTTP, HTML and CSS) for publishing posts to your site.  So how exactly
would one able to even recognize that a piece of content on someone's
website was a "post" that could be "replied to" or "liked" at all?

These are important, fundamental questions if you're trying to understand
how a social network functions, particularly a decentralized one.  It boils
down to asking:

* How and where are posts stored?
* How does software read or consume the posts?
* What do the posts look like?

The question of how posts are stored is easy to answer, because the IndieWeb
community doesn't specifically answer it.  A person's posts are stored on
their website, in whatever way that person sees fit.  In a very real sense,
every IndieWeb enabled website implicitly fronts a "database" (to use the
term loosely) of posts and in this manner, all the collective posts of the
IndieWeb community are spread out over the Internet.

*Consumption* of an IndieWeb user's posts (by a third party reader, for
example) is accomplished by hitting the same URL that one would use to read
their content, i.e. the same URL that you'd type in a browser address bar.
Every IndieWeb enabled website effectively doubles as both a web *page* and
a web *service*.  It's the ultimately REST architecture.

This naturally leads to the question of how 


In the past, the answer to these questions tended to be technologies like
[RSS][12] or [Atom][13], which effectively required you to repackage your
content in a separate feed, in a separate format, usually XML.  The IndieWeb
community, on the other hand, favours a standard called [*microformats*][7].
Microformats are effectively the API of the IndieWeb.

Microformats are unobtrusive annotations and/or markup added to your
existing content - no separate feed needed.  They're basically just
specialized CSS classes that you add to your posts to make it possible to
extract various pieces of information in a standardized way.

For example, a standard post is designated with the [h-entry][10]
microformat.

    <div class="h-entry">
       This is a post.
    </div>

All that's required here is that your post is surrounded by tags that
incorporate a h-entry CSS class.  Beyond that, you can structure your post
however you see fit.

### Annotating your Identity

Level 2 also involves augmenting your personal identity with [h-card][11]
microformat information.  The h-card microformat allows the owner of a
website to embed useful bits of personal information like one's name, photo,
and email address.

A properly embedded h-card becomes especially important when you want your
personal information to appear correctly in a context other than your own
website - for example, when posting likes and replies (more on that later).
