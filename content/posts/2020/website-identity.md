title: Your Website is Your Passport
date: 2020-02-05 16:30:11
modified: 2020-02-05 16:30:11
status: draft

One of the themes that crops up again and again in the [IndieWeb][]
community is that your personal domain, with attendant website, should form
the nexus of your online existence.  Of course, people can and do maintain
separate profiles on a variety of private social media platforms, but these
remain subordinate to the identity represented by your personal website,
everyone's one-stop-shop for all things *you* and the central hub out of
which your other identities radiate.

Part of what this means in practice is that your domain should function as a
kind of universal online passport, allowing you to sign in to various
services and applications by simply entering your personal URL and hitting
enter.

How is this accomplished?  There is a short answer and there is a long
answer.

## For the Impatient

The simplest (though not the only) way to leverage your website for sign-in
purposes is to delegate the authentication process to an existing social
media profile.

First, add a special "me" anchor tag to your home page detailing where to
find the profile you want to use.  Let's say, for the sake argument, that
you want to use your [Github][] account.  The link would look like this:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it like any other link on your home page.
Obviously, replace the "drivet" part with your own username.

Next, edit your Github profile so that the Website field points back to your
root domain.  You do this to show that you actually control the Github
account to which your homepage is pointing:

<div style="clear: both; text-align: center;">
<img border="0"
     src="{attach}github_profile.png" 
     alt="Github profile" />
</div>

Finally, you add this link tag to the head of your homepage:

    <head>
        ....
        <link rel="authorization_endpoint" href="https://indieauth.com/auth">
    </head>

You should now be able to sign in to, for example, a website like
[indieweb.org][].  You can try it now by going to the site and clicking the
"Log in" link.

You'll be presented with a text box into which you can enter you personal
domain. The service will look for an authorization_endpoint link in your
homepage, and will delegate the authentication procedure to the first "me"
link it finds.  Obviously, if you use this procedure, you are still
dependant on an external social networking profile for authentication
purposes, which is less than ideal, but at least the process starts with
your own domain, and there are ways to detach yourself from your external
profiles completely if you wish to go that far (see, for example, the
[selfauth][] project).

Please note that what I've just described is an *authentication* procedure.
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

## For the Less Impatient: A Brief Detour Into OAuth-land

The process of using your domain to sign in to sites and services is called
*web sign-in* and is implemented via a protocol called IndieAuth, a specific
flavour of OAuth allowing for decentralized authentication.

(When I speak of "OAuth", I refer to OAuth 2.  Although there is such a thing
as OAuth 1, it's rarely used nowadays, and is therefore not pertinent to
this discussion)

Understanding IndieAuth requires a basic knowledge of OAuth and though there
are tons of OAuth resources available online, I've had difficulty funding
any that give me the right level of detail - it's always either too much or
too little.  Hence the reason for this detour; I will try and outline (what
I consider to be) the salient features of OAuth from the perspective of
someone (me) who routinely becomes confused about the topic.  I will then
try explaining where IndieAuth fits into the picture.

BY the way, you don't need to know any of this if you're just trying to do
get IndieAuth working for your domain.  What follows is strictly for the
curious.

### What Problem Does OAuth Solve?

Let's say you want to show your latest tweet on your blog.  How would one go
about doing this?

As it turns out, Twitter provides a REST API for exactly this purpose.  But
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

In other words, OAuth is meant to allow you to give applications limited
access to resources without having to give away your full credentials.

### The Shape of OAuth

The "auth" in OAuth stands for *authorization*, not *authentication* and,
fundamentally, OAuth is an authorization protocol, not an authentication
protocol.

What does this mean, exactly?  Broadly speaking, it means that OAuth is all
about managing *access* to web resources - like tweets - and *not* about
managing the *identities* of those trying to access them.

It can get confusing because authentication is, as you'll see later, baked
into the protocol during a couple of key steps.  But these authentication
steps exist merely in service to

The spec defines several actors:

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
calls via the Authorization header:

    GET /api/blah
    Authorization: Bearer 128728364872

It sounds like a tautology but, simply put, access tokens grant the
application access to the API.  So how do we go about getting one?

### The Authorization Code Flow

The OAuth standard defines several "flows" or procedures for obtaining an
access token, but only one of them is really important for our purposes: the
authorization code flow.  It is, roughly, a two step process.

First, the client (i.e. the blogging application, in our example) obtains an
*authorization code* from the authorization server by providing a client
identifier and a list of requested *scopes*, detailing what the client is
wants to do with the resource.  The end user is then authenticated to the
authorization server (the exact mechanism of which can vary from provider to
provider), after which they consent (or not) to the scopes provided.

Second, the client trades that authorization code for an access token,
possibly authenticating with a client secret at the same time.

### Client Registration

In all OAuth flows, the authorization server requires a priori knowledge of
the client attempting to access the resource.  To use the ongoing example,
Twitter's authorization server needs to know that your blogging application
will be trying to access your tweets.

Most often, this entails explicit client registration.  Several pieces of
information need to be provided:

* The client identifier. A string used to identify the client.
* A redirect URL.  The URL to which the browser will be returned once the
  authorization code has been issued.
* Some implementations require (or generate) a client secret.  This will be
  used during the final phase of the procedure, when the client trades the
  authorization code for an access token.
