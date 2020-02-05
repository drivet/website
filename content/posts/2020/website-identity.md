title: Your Website is Your Passport
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

One of the themes that crops up again and again in the IndieWeb community is
that your personal domain, with a website attached to it, should form the
nexus of your online existence.  On the IndieWeb, even if you *also* spread
yourself across a multitude of different social media sites, these profiles
nonetheless remain subordinate to your personal website - the central hub
out of which your other identities radiate, and everyone's one-stop-shop for
all things *you*.

Part of what this means in practice is that you should be able to use your
domain as a kind of universal online identifier or passport, using it to
sign in to various services and applications.  We've all seen websites
featuring "Sign in with Facebook" and "Sign in with Google" buttons.  The
idea here is to be able to do the same thing with your personal URL.

How is this accomplished?  There is a short answer and there is a long
answer.

## For the Impatient

The simplest way to leverage your website for sign-in purposes is to delegate
the authentication process to an existing social media profile.

First, add a special "me" anchor tag to your home page detailing where to
find the profile you want to use.  Let's say, for the sake argument, that
you want to use Github account.  The link would look like this:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it like any other link on your home page.
Obviously, replace the "drivet" bit with your own username.

Next, edit your Github profile so that the Website field points back to your
root domain.  You do this to show that you actually control the Github
account to which your homepage is pointing.

Finally, you add this link tag to the head of your homepage:

    <head>
        ....
        <link rel="authorization_endpoint" href="https://indieauth.com/auth">
    </head>

You should now be able to sign in to, for example, a website like
indieweb.org.  Try it now by going to the site and clicking the "Log in"
link.

You'll be presented with a text box into which you can enter you personal
domain. The service will look for an authorization_endpoint link in your
homepage, and will delegate the authentication procedure to the first "me"
link it finds.  Obviously, if you use this procedure, you are still
dependant on an external social networking profile for authentication
purposes, which is less than ideal, but at least the process starts with
your own domain, and there are ways to detach yourself from your external
profiles completely if you wish to go that far (see, for example, the
selfauth project).

Please note that what I've just descibed is an *authentication* procedure.
It's enough to get you logged into to websites which support the protocol.
It is *not*, by itself, an authorization procedure -it won't grant you
access to any APIs, for example, and it won't let use things like Micropub
or Microsub out of the box.  For that to work, you need to obtain a token
after authenticating - read on if you want to know why.  Luckily, that's
pretty easy to do as well if you're willing to rely on an external service.
Just add the following link to the head of your website:

    <head>
        ....
        <link rel="token_endpoint" href="https://tokens.indieauth.com/token"/>
    </head>

And that's pretty much it.  Easy, right?

## For the Less Impatient (or the Simply Curious)

The process of using your domain to sign in to sites and services is called
*web sign-in* and is implemented via a protocol called IndieAuth, a specific
flavour of OAuth 2 - the same protocol powering all those "Sign in with
Google" buttons - but filling in a lot of the details and adding some new
ones, in order to allow for truly decentralized authentication.

There are a ton of OAuth 2 resources available online and I will not pretend
that I can do a better job summarizing this rather complex subject.  That
being said, I *have* found it difficult finding resources that give, for me
at least, the right level of detail and so I'll try and outline what I feel
are some of the more pertinent points here, and I'll try and show how all
this relates to the IndieAuth protocol.

### The Basic OAuth Flow - A Recap

Let's say you have a blog, and you want to show the latest 10 tweets from
your twitter timeline on said blog.  How do you do it?

Twitter provides a REST API for exactly this purpose.  But you don't want
just anyone using it.  So how do you secure it?

In the past, a problem like this may have been solved by giving your blog
access to your username and password, so that it could pass them to the
Twitter API, thus allowing access to your feed.  This, obviously, has
various problems:

* You need to configure your password somewhere, probably in plain text.
  This is insecure.
* You're giving your blog full access to your Twitter account, even though
  all it needs to do it read a few tweets off the top.
* What if your password gets compromised?

OAuth 2 is meant to help with these problems.  There's an excellent analogy
on oauth.net:

    Many luxury cars today come with a valet key. It is a special key you give
    the parking attendant and unlike your regular key, will not allow the car to
    drive more than a mile or two. Some valet keys will not open the trunk,
    while others will block access to your onboard cell phone address
    book. Regardless of what restrictions the valet key imposes, the idea is
    very clever. You give someone limited access to your car with a special key,
    while using your regular key to unlock everything.

Broadly speaking, OAuth is about managing access to web resources - like
tweets.  It defines several entities;

* The user, or the one who owns the resources.  In the above example, that
  would be the person who is trying to put their timeline on their blog.
* The client, or the entity acting on behalf of the user.  This would be the
  blogging software, in the above example.
* The resource service.  This would be Twitter's tweet API.

Clients need to be registered with the resource service.  To use the ongoing
example, you need to tell Twitter that you blogging software will be trying
to access your tweets.  Among other things, two key pieces of information
need to be provided:

* A client identifier. This is a string used to identify the client.  This
  is considered public information
* A redirect URL.  This is the URL to which the browser will be returned once 
