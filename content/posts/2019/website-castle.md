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

## Going Further: Posting Content

As I've alluded to before, the IndieWeb is an attempt to make a social
network out of the web itself.  More than that, however, it's an attempt to
formalize, generalize and modernize the notion of a personal blog.

Central to this idea are the twin concepts of [posts][6] and
[microformats][7].  A post is, roughly speaking, a piece of chronologically
ordered content.  The IndieWeb recognizes many different kinds of posts, but
the two most common ones are probably [*articles*][8] (corresponding to
classic blog entries) and [*notes*][9] (corresponding to what other services
call tweets or status updates).

Remember, though, that the IndieWeb does not prescribe any particular
blogging engine or, indeed, any particular technology at all (other than
standard HTML and CSS) for publishing your site.  So how exactly does one
"share" a status update in a way that another site can use?

It's an important question - probably the first and most fundamental of
questions if you're dealing with a social networking service like Twitter.
It boils down to asking:

* What is the format of a post?
* How is it stored? 
* How does one read it?

In the past, the answer to these questions were technologies like [RSS][12]
or [Atom][13], which effectively required you to repackage your content in a
separate feed, usually as XML.  For the IndieWeb, this is instead
accomplished via something called *microformats*.  Microformats are
effectively the API of the IndieWeb.

Microformats are unobtrusive annotations and/or markup added to your
existing content - no separate feed needed.  For the most part, they're
basically just specialized CSS classes that you add to your posts to make it
possible to extract various pieces of information in a standardized way.

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
