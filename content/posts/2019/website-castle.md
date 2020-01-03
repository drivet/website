title: Websites and Castles
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

In a [previous blog post][1], I gave a very brief, high level introduction
to the [IndieWeb][5], hopefully giving a sense of what is it and why it
matters.  In this post I'll zoom in a little bit and explain something of
the mechanics of how the IndieWeb actually works and what it means to "join"
(as well as what it means to "like" a post or "share" a status update).

So, what does it take to join the IndieWeb?  Or, to put it another way, what
turns a plain, vanilla website into an IndieWeb enabled one?  The IndieWeb
community's [answer][2] to this question involves 5 different compliance
"levels", which is okay if you're trying to collect "indieweb cred", I
suppose, but which gets a bit daunting if you're new to the whole thing.  So
this post will take a different tack and just give a high level overview of
the typical features common to most IndieWeb enabled sites and, roughly, how
they work.

## The Bare Minimum: Owning your own Identity

They say a person's home is their castle, and this is especially true when
it comes to the IndieWeb - except, of course, that with the IndieWeb, a
person's *website* is their castle.

So the first thing you need to join the IndieWeb is, obviously, a classic,
personal website and, more than that, it has to be *hosted on a domain that
you control*.  This means that a renting a space under a domain you *don't*
control (in the style of https://notmydomain.com/~myname, for example) won't
do.

But having your own website on your own domain, while a necessary first
step, is not sufficient.  In addition, you need to be able to use that
domain to sign into other services using [IndieAuth][3], a login protocol
based on OAuth2.

In general, this means embedding your home page with various bits of
information which can be used to figure out who you are.  There are numerous
ways to do this, but one easy way involves using the [IndieAuth.com][4]
service (distinct from the IndieAuth protocol) and delegating to a social
networking profile of your choice.  What does that even mean?

Well, first it means adding a special "me" anchor tag to your home page
detailing where to find the profile you want to use for authentication
purposes.  You can, for example, use your Github account for this purpose:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it for regular navigation purposes, like any other
link on your home page.

Next, in your Github profile, you need to make sure you include a link back
to your domain, to show that you actually control that account.  A "me" link
is not valid unless it point to a profile that points back to your homepage.

Finally, you add a special link tag to the head of your home page:

    <link rel="authorization_endpoint" href="https://indieauth.com/auth">

The URL included here is the service which will actually perform the
IndieAuth process.

Signing in to an IndieAuth enabled service is usually just a matter of
entering your full domain in a text box.  The protocol will look for an
authorization_endpoint link tag in your homepage, and will delegate the
authentication procedure to the first valid "me" link it finds.  Obviously,
if you use this procedure, you are still dependant on an external social
networking profile for authentication purposes, which is less than ideal,
but at least the process starts with your own domain, and there are ways to
detach yourself from your external profiles completely if you wish to go
that far.

## Posting Content and Having Conversations

At the heart of the IndieWeb is an attempt to unify the ideas behind
personal websites, blogs and social networks, but in a manner consistent
with how the world wide web operates.

Central to this vision is the concept of a [post][6].  A post, roughly
speaking, is simply a piece of chronologically ordered content appearing on
your website, identifiable by a unique URL called a [permalink][17].  It's
hard to underestimate their importance; they are the fundamental building
blocks from which IndieWeb conversations are built.  They are the main
mechanism by which one recreates, in a decentralized manner, the kinds of
online interactions one has come to expect from private social networks.

In the IndieWeb, almost all forms of content are considered posts, even
things that one would not normally think of as a post.  In particular, we
have:

* [*articles*][8].  These are the equivalent of classic blog entries -
  titled, long form pieces of writing.
* [*notes*][9].  These correspond to what other services might call tweets or
  status updates - short, titleless bits of content.
* [*reposts*][15]. These correspond to what other services might call
  "retweets" or "shares" - posts which parrot other posts verbatim.
* [*replies*][14]. These are bits of content written in reply to a post on
  another website.
* [*likes*][16].  These are posts which represent the act of liking another
  post.

Conceptually, articles and notes are probably the easiest to grasp, and the
easiest to fit into the "post" mould.  Reposts are a bit more abstract, but
still pretty straightforward, because it's still easy to see how they belong
on *your* website, even if you're shamelessly stealing the content from
someone else.

Replies in an IndieWeb context might require some conceptual adjustment if
you're used to posting comments on standalone blogs. In the latter case,
your reply ends up being trapped on someone else's site or service, an
outcome which is anathema to the IndieWeb community.  Instead, a reply post
is always on *your own* site, even though it refers to a post on another
site.

As mentioned above, a "like", in the IndieWeb community, is also considered
a kind of post and this requires, perhaps, even more conceptual adjustment.
People tend to think of a "like" as an *action* applied to a post on another
site, rather than content living on your own.  The IndieWeb community begs
to differ on this point and treats your "like" as if it were just another
one of your posts, albeit one who's content, like a repost, refers almost
entirely to *another* post.  In that sense, a like and a repost are almost
exactly the same in terms how they're structured (i.e. they are both posts
which derive their content by referring to an external post) and differ
merely in the meaning they are intended to convey.

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


[1]: /2019/intro-to-indieweb
[2]: https://indieweb.org/IndieMark
[3]: https://indieweb.org/IndieAuth
[4]: https://indieauth.com
[5]: https://indieweb.org
[6]: https://indieweb.org/posts
[7]: https://indieweb.org/microformats
[8]: https://indieweb.org/article
[9]: https://indieweb.org/note
[10]: https://indieweb.org/h-entry
[11]: https://indieweb.org/h-card
[12]: https://en.wikipedia.org/wiki/RSS
[13]: https://en.wikipedia.org/wiki/Atom_(Web_standard)
[14]: https://indieweb.org/reply
[15]: https://indieweb.org/repost
[16]: https://indieweb.org/like
[17]: https://indieweb.org/permalink
