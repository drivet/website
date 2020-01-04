title: Websites and Castles
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

In a [previous blog post][1], I gave a very brief, high level introduction
to the [IndieWeb][5], hopefully giving a sense of what is it and why it
matters.  In this post I'll try and zoom in a tiny bit and explain something
of the mechanics of how the IndieWeb actually works and what it means to
"join" (as well as what it means to "like" a post or "share" a status
update).  Further posts will go into more details.

## The Bare Minimum: Owning your own Identity

They say a person's home is their castle, and this is especially true when
it comes to the IndieWeb - except, of course, that with the IndieWeb a
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

In general, this involves embedding your home page with various bits of
information which can be used by various services to figure out who you are.
There are numerous ways to do this, but one easy way involves using the
[IndieAuth.com][4] service (distinct from the IndieAuth protocol) and
delegating to a social networking profile of your choice.  What does that
even mean?

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

## Posting Content and Avoiding Solipsism

At the heart of the IndieWeb is an attempt to unify the ideas behind
personal websites, blogs and social networks, but in a manner consistent
with how the world wide web operates.

Central to this vision is the concept of a [post][6].  A post, roughly
speaking, is simply a piece of chronologically ordered content appearing on
your website, identifiable by a unique URL called a [permalink][17].  It's
hard to underestimate their importance; they are the fundamental building
blocks from which IndieWeb conversations are built.  They are the main data
by which one recreates, in a decentralized manner, the kinds of online
interactions one has come to expect from private social networks.

If you come from a Facebook background, your website is basically your
"wall".  It houses all your posts, and they remain under your control.  As I
alluded to before, your website is your castle.

In the IndieWeb, almost all forms of content are considered posts, even
things that one would not normally think of as posts.  In particular, we
have:

* [*articles*][8].  These are the equivalent of classic blog entries -
  titled, long-form pieces of writing.
* [*notes*][9].  These correspond to what other services might call tweets or
  status updates - short, titleless bits of content.
* [*reposts*][15]. These correspond to what other services might call
  "retweets" or "shares" - posts which re-publish other posts verbatim.
* [*replies*][14]. These are bits of content written in reply to a post on
  another website.
* [*likes*][16].  These are posts which represent the act of liking another
  post.

Articles and notes are probably the most familiar of these, and are probably
what most people think of when they think of a "post".  They are pieces of
writing which make sense "on their own", so to speak; they are not, strictly
speaking, "about" anything else.  Reposts, replies and likes, on the other
hand, are collectively "about" other pieces of content and they only make
sense in the context of that other content.

The concept of a repost will be familiar to any user of Twitter (where the
feature is called a *retweet*) and its casting as a new post on *your own*
site (despite the fact that its content is completely derived from another
post from another site) probably makes sense in that context.

Reply posts, in an IndieWeb context, might require some conceptual
adjustment if you're used to posting comments on standalone blogs. In the
latter case, your reply ends up being trapped on someone else's site or
service, an outcome which is anathema to the notion of owning your own data.
Instead, like all posts, an IndieWeb reply is always on *your own* site,
even though it refers to another post on some other site.

In the same vein, and perhaps requiring even more conceptual adjustment, an
IndieWeb "like" is *also* considered a kind of post.  It's a bit weird to
formulate it this way, since people tend to think of a "like" as an *action*
applied to a post on another site, rather than content living on your own.
The IndieWeb community begs to differ on this point and treats your like as
if it were just another one of your posts, albeit one who's content refers
almost entirely to *another* post (in the same fashion as a repost or a
reply).  In that sense, likes, reposts, and replies are all almost exactly
the same in terms how they're structured on an IndieWeb site (i.e. they are
all posts which derive at least part of their content by referring to an
external post) and differ merely in the meaning they are intended to convey.

An obvious question arises at this point: after you've liked (or reposted,
or replied to) a post, how do you communicate that fact to the website
owner?  It seems like the sort of thing they'd want to know; many websites,
for example, display a count of likes and reposts under the post itself.
The answer to this issue involves the twin concepts of [webmentions][19] and
[microformats][20], but I will save the details for another post.

## On Not Losing Your Friends

It's all well and good to talk about owning your own content but the fact
remains that most people are not on the IndieWeb.  How do you deal with
people who are using sites like Twitter or Facebook?  Are they forever
deprived of your wonderful content?

This is always a bit of a glaring hole when talking about new social
networks.  A social network's value is at least partly derived by its size
(i.e. how many people see your post), and if the network is small, it's of
limited value.

The IndieWeb's answer to this dilemma, as usual, is not to prescribe any
particular technology but rather to coin an acronym: [POSSE][18], or Publish
(on your) Own Site, Syndicate Elsewhere.  The idea is to publish a post on
your own site *first* and then, only after it's available there via its
permalink, copying a version of the post to whatever other social networks
you wish.

There are lots of ways to do this, and it's strongly dependent on what
software you use to publish your website.  Lots of people do it manually;
they will just copy the content to wherever it needs to go.  Some blogging
engines, like Wordpress, support automatic syndication to the social network
of your choice.  I myself use a service called [Bridgy][21] to syndicate my
posts to Twitter.

Once your post has been published to a social network, the question then
arises of how to get notified when people interact with your *syndicated*
post.  In other words, what happens when someone likes your post *on
Twitter*?  The IndieWeb community calls this process [*backfeed*][22] and
your options for this vary wildly depending on the APIs that are available
for the sites you use.  I myself just use Bridgy since it supports backfeed as
well as syndication.


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
[18]: https://indieweb.org/POSSE
[19]: https://indieweb.org/webmention
[20]: https://indieweb.org/microformats
