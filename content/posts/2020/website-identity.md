title: Your Website is Your Passport
date: 2020-02-05 16:30:11
modified: 2020-02-05 16:30:11
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
It is *not*, by itself, an authorization procedure - it won't grant you
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
flavour of OAuth 2 allowing for decentralized authentication.  Although
there is such thing as OAuth 1, it's rarely used nowadays, and so henceforth
I shall refer to OAuth 2 as simply OAuth and leave it at that.

There are a ton of OAuth resources available online but I have found it
difficult finding one that give, for me at least, the right level of
detail - it's always either too much or too little - and so I'll try and
outline what I feel are some of the more pertinent points here, and I'll try
and show where IndieAuth fits in all this all this.

Understanding IndieAuth requires a basic knowledge of OAuth but, that being
said, you don't need to know any of this if all you're trying to do is get
IndieAuth working for your domain.  What follows is stricly for the curious.

### What Problem Does OAuth Solve?

Let's say you want to show your last 10 tweets on your blog.  How would one
go about doing this?

We are in luck! Twitter provides a REST API for exactly this purpose.  But
Twitter doesn't want just anyone looking at your tweets.  So how is the API
secured?

In the past, a problem like this may have been solved by giving your blog
access to your Twitter username and password, so that it could pass them to
the Twitter API, thus allowing access to your feed.  This works, but has
several problems:

* You need to configure your password somewhere, probably in plain text.
  This is insecure.
* You're giving your blog full access to your Twitter account, including
  write access, even though all it needs to do it read a few tweets off the
  top.
* What if your password gets compromised?

OAuth is meant to help with these problems.  There's an excellent analogy on
oauth.net:

> Many luxury cars today come with a valet key. It is a special key you give
> the parking attendant and unlike your regular key, will not allow the
> car to drive more than a mile or two. Some valet keys will not open the
> trunk, while others will block access to your onboard cell phone address
> book. Regardless of what restrictions the valet key imposes, the idea is
> very clever. You give someone limited access to your car with a special
> key, while using your regular key to unlock everything.

Broadly speaking, OAuth is a protocol or framework for managing access to
your own web resources - resources like, for example, you tweets.  It
defines several actors:

* The *end user*, or the one who owns the resources.  In the above example,
  that would be the person who is trying to put their tweets on their blog.
* The *client* or the application acting on behalf of the user.  This would
  be the blogging application, in the above example.
* The *resource service*.  This would be Twitter's API.  It's assumed that
  the end user has an account with Twitter.
* The *authorization server*, existing alongside the resource service.  This
  manages the actual OAuth protocol, so your blog can get access to those
  tweets.

The central idea behind OAuth is that the end user delegates resource access
to the client application, so that the application can access the resources
on the user's behalf.  The final result of this delegation process is an
opaque string called an access token that is meant to be included in the API
calls via HTTP header.

It sounds like a tautology but, simply put, access tokens grant the
application access to the API.  So how do we go about getting one?

### OAuth Flows

The OAuth standard defines several "flows" or procedures for obtaining an
access token.  Not all of them are important for our purposes, so I'm going
to focus on just a couple.

The most popular one would probably be the authorization code flow.  It is,
roughly, a two step process.

First, the end user obtains an *authorization code* by providing a client
identifier and a list of *scopes*, detailing what the client is allowed to
do with the API, and then authenticating to the authorization server (the
exact mechanism of which can vary from provider to provider).

Second, the client trades that authorization code for an access token,
possibly authenticating with a client secret at the same time.



### Client Registration

Clients need to be registered with the authorization server.  To use the
ongoing example, you need to tell Twitter's authorization server that your
blogging application will be trying to access your tweets.  Several pieces
of information need to be provided:

* A client identifier. This is a string used to identify the client.  This
  is considered public information
* A redirect URL.  This is the URL to which the browser will be returned once 
* (Optional) A client secret.  This will be used 

### Where Does IndieAuth Fit?
