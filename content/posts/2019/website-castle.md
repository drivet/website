title: Websites and Castles
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

In a [previous blog post][1], I gave a very brief, high level introduction
to the [IndieWeb][5] - what is it and why would one care?  In this post I'll
zoom in a little bit and explain something of the mechanics of how the
IndieWeb actually works and what it means to "join" it (as well as what it
means to "like" a post or share a status update).

## IndieMark Levels

So, what does it take to join the IndieWeb?  Or, to put it another way, what
turns a standard, vanilla website into an IndieWeb enabled one?  The
IndieWeb community's answer to this question is that you can do it in
[levels][2]:

1. Own your own identity
2. Post notes and POSSE
3. Post replies and send webmentions
4. Receive & display comments
5. Comments CRUD

A lot of these terms will be unfamiliar if you're just starting to learn
about the IndieWeb.  Don't worry, I'll explain what each of these terms
mean.

## Level 1 - Owning your own Identity

They say a person's home is their castle, and this is especially true when
it comes to the Indieweb - except, of course, that with the IndieWeb, a
person's *website* is their castle.

So the first thing you need to join the IndieWeb is a classic, personal
website, hosted on a domain that you control.  That means that a renting a
space under someone else's domain (in the style of
https://notmydomain.com/~myname, for example) won't do; the domain itself
has to be under your control,

But having your own website on your own domain, while necessary, is not
sufficient.  In addition, you need to be able to use that domain to sign
into other services using [IndieAuth][3], a login protocol based on OAuth2.

In general, this means embedding your home page with various bits of
information that services can use to figure out who you are.  There are
numerous ways to do this, but one easy way involves using the
[IndieAuth.com][4] service (distinct from the IndieAuth protocol) and
delegating to a social networking profile of your choice.  Specifically, you
can:

1. Add a special "me" anchor tag to your home page detailing where to find
   the profile you want to use for authentication purposes.  You can, for
   example, use your Github account for this purpose:


    <a href="https://github.com/drivet" rel="me">Github</a>


   Note that there is nothing special about this link, aside from the "me"
   attribute.  You can use it for regular navigation purposes, like any
   other link on your home page.

2. In your Github profile, make sure you include a link back to your domain
   (i.e. adding random Github profiles to your homepage won't work unless
   you have access to those accounts).
   
3. Add a special link tag to the head of your home page:

    <link rel="authorization_endpoint" href="https://indieauth.com/auth">


Signing in to an IndieAuth enabled service is usually just a matter of
entering your full domain in a text box.  The protocol will look for an
authorization_endpoint link tag in your homepage, and will delegate the
authentication procedure to the first "me" link it finds.  The "me" links
are considered valid if the social networking profile contains a link back
to the original domain. Obviously, if you use this procedure, you are still
dependant on an external social networking profile for authentication
purposes, which is less than ideal, but at least the process starts with
your own domain, and there are ways to detach yourself from your external
profiles completely if you wish to go that far.

If you read the wiki, there's a bit more to unlocking Level 1 that just have
an IndieAuth enabled personal domain, but I would argue that the key feature
is the authentication, and that this would be the bare minimum required to
join the IndieWeb.

## Level 2 - Posting Content

As I've alluded to before, the IndieWeb is an attempt to make a social
network out of the web itself.  More than that, however, it's an attempt to
formalize, generalize and modernize the notion of a personal blog.
IndieMark Level 2 encapsulates this latter idea, and unlocking it requires
adding different forms of content to your website.

Central to this idea are the twin concepts of [posts][6] and
[microformats][7].  A post is, very generally, a piece of chronologically
ordered content.  The IndieWeb recognizes many different kinds of posts, but
the two most common ones are probably [*articles*][8] (corresponding to
classic blog entries) and [*notes*][9] (corresponding to what other services
might call tweets or status updates).  You need to have at least a couple of
notes and articles on your site for it to be eligible for level 2.

Remember, though, that the whole point of this exercise is to be able to
cobble together some semblance of a social network out of a bewildering
variety of personal websites.  This means that everyone's posts need to have
some form of standardized structure.

This is accomplished via something called *microformats*.  Microformats are
effectively the API of the IndieWeb.  It's the way one achieves
interoperability between websites which are as different as they are
numerous.

The key thing to note about microformats is that they are designed to be
unobtrusive. They're basically just specialized CSS classes that you add to
your posts to make it possible to extract various pieces of information in a
standardized way.

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
