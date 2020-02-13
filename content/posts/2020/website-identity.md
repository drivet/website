title: Your Website is Your Passport
date: 2020-02-05 16:30:11
modified: 2020-02-05 16:30:11
status: draft

One of the themes that crops up again and again in the [IndieWeb][1]
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

How is this accomplished?  There is a short answer and there is a longer
answer.

## For the Impatient

The simplest (though not the only) way to leverage your website for sign-in
purposes is to delegate the authentication process to an existing social
media profile.

First, add a special "me" anchor tag to your home page detailing where to
find the profile you want to use.  Let's say, for the sake argument, that
you want to use your [Github][2] account.  The link would look like this:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it like any other link on your home page.
Obviously, replace the "drivet" part with your own username.

Next, edit your Github profile so that the Website field points back to your
root domain.  You do this to show that you actually control the Github
account to which your homepage is pointing:

<div style="clear: both; text-align: center;">
<img border="0"
     src="{attach}github_profile.jpg" 
     alt="Github profile" />2
</div>

Finally, you add this link tag to the head of your homepage:

    <head>
        ....
        <link rel="authorization_endpoint" href="https://indieauth.com/auth">
    </head>

You should now be able to sign in to, for example, a website like
[indieweb.org][1].  You can try it now by going to the site and clicking the
"Log in" link.

You'll be presented with a text box into which you can enter you personal
domain. The service will look for an authorization_endpoint link in your
homepage, and will delegate the authentication procedure to the first "me"
link it finds.  Obviously, if you use this procedure, you are still
dependant on an external service (indieauth.com) and an existing social
networking profile for authentication purposes, which is less than ideal,
but at least the process starts with your own domain, and there are ways to
detach yourself from your external profiles completely if you wish to go
that far (see, for example, the [selfauth][4] project).

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

Once again, if using an external service bothers you, you can host your own
token service.

And that's pretty much it.  Easy, right?  You can stop reading right now if
you're not interested in any of the details, or you can read on if you are.

## For the Less Impatient: A Brief Detour Into OAuth-land

The process of using your domain to log in to sites and services is called
*web sign-in* and is implemented via a protocol called [IndieAuth][5], a
specific flavour of [OAuth][6] allowing for decentralized authentication.

(When I speak of "OAuth", I refer to OAuth 2, not OAuth 1, as it's rarely
used nowadays, and is therefore not pertinent to this discussion)

Understanding IndieAuth requires a basic knowledge of OAuth, which is a
daunting subject if you've never dealt with it before (and even if you
have).  I'm going to try and give just enough information here to illustrate
where IndieAuth fits into this landscape, but if you want more information I
highly recommend reading the resources at [oauth.com][9]; I find they strike
a good balance of detail, especially if you have a modicum of programming
and HTTP experience.

### What Problem Does OAuth Solve?

The "auth" in OAuth stands for *authorization* (*not* authentication) and,
fundamentally, OAuth is an authorization protocol, not an authentication
protocol.  What this means is that OAuth is all about managing *access* to
online resources (like REST APIs) and not about the *identity* of the user
whose resources are being accessed.

The textbook example is that of a printer application A that prints photos
from a photo sharing application B (assume that the applications are managed
by different business entities).  In the past, a problem like this may have
been solved by configuring your credentials for B somewhere in A, but that
has several issues, not the least of which is that A now has full access to
your entire account in B, even though all it needs to do is print out a few
photos.

OAuth is designed to help with this problem.  It's meant to allow you to
give application limited access to resources from another service without
having to give away your full credentials.  It does this by issuing *tokens*
representing the resources the application wishes to access, along with the
things the application is allowed to do to with those resources.

The concept of a token is not unlike the concept of hotel room access card.
The access card lets you into your own room, but it doesn't grant you access
to the entire hotel; you can't use it to go into another room, for example,
and you certainly can't use it to go into the staff areas.

Also, notably, *your name and photo are not on the access card*.  Your
access card isn't a piece of identification.  Someone who stole your
driver's licence would have a hard time using it as a driver's licence
because their name and face don't match what's on the card.  Someone who
stole your access card, on the other hand, would have no trouble ransacking
your room.  This is part of what is meant when people say that OAuth is
about authorization and *not* authentication.

And yet, even so, there are subtleties in that distinction that are
understandably confusing.  The process of obtaining your hotel access key,
for example, will almost certainly involve an authentication step - you'll
probably have to show your passport or driver's licence to the front desk.
In the same vein, and pretty much for the same reason, the OAuth protocol
*does* include one or two authentication steps as well, before the token is
issued.

This leads some people to conclude that OAuth can be used as an
authentication protocol, and they're *almost* right, which makes it all the
more insidious.  It's actually not that difficult to build an authentication
protocol on top of OAuth but

### OAuth's Moving Parts

The OAuth [spec][8] defines several actors:

* The *end user*, or the one who owns the resources.  In the above example,
  that would be the person who is trying to print their photos.
* The *client* or the application acting on behalf of the user.  This would
  be the printing application (A), in the above example.
* The *resource service*.  This would be the photo shraing service (B).
* The *authorization server*, existing alongside the resource service.  This
  manages the actual OAuth protocol.

The central idea behind OAuth is that the end user delegates resource access
to the client application, so that the application can access the resources
on the user's behalf.  The final result of this delegation process is an
opaque string called an access token that is meant to be included in the API
calls via the HTTP Authorization header:

    GET /api/blah
    Authorization: Bearer 128728364872

It sounds like a tautology but, simply put, access tokens grant the
application access to the API.  So how do we go about getting one?

### The Authorization Code Flow

The OAuth standard defines several "flows" or procedures for obtaining an
access token, but only one of them is really important for our purposes: the
authorization code flow.  It is, very roughly, a two step process.

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
* Many implementations require (or generate) a client secret.  If present,
  this will be used during the final phase of the procedure, when the client
  trades the authorization code for an access token.

[1]: https://indieweb.org/
[2]: https://github.com/
[4]: https://github.com/Inklings-io/selfauth
[5]: https://www.w3.org/TR/indieauth/
[6]: https://en.wikipedia.org/wiki/OAuth
[7]: https://oauth.net/about/introduction/
[8]: https://tools.ietf.org/html/rfc6749
[9]: https://www.oauth.com/
