title: Your Website is Your Passport
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

One of the themes that crops up again and again in the IndieWeb community is
that your personal website should form the nexus of your online identity.
Obviously, people can and do spread their identity across a multitude of
different social media sites like Twitter or Facebook but such accounts
should always be considered subordinate to your personal website, which
remains everyone's one-stop source of truth for everything *you* related.

Among other things, what this means in practice is that you should be able
to use your domain to sign in to services and applications which support it.
We've all seen the "Sign in with Facebook" and "Sign in with Google"
buttons.  What if you could do the same thing with your personal URL?  What
if your website acted as a kind of online passport?

The process of using your domain to sign in to sites and services is called
*web sign-in* and is implemented via a protocol call IndieAuth, a specific
flavour of OAuth 2 - the same protocol powering all those "Sign in with
Google" buttons - but allowing for truly decentralized authentication.

OAuth 2 itself is a beast.  Part of what makes it so complicated is that
it's less of a protocol and more of an authorization framework; the standard
tries to cover a lot of different scenarios (web, mobile, and single page
applications) whilst simultaneously leaving a lot unspecified (like client
registration, the specific authentication mechanism used).  IndieAuth fills
in a lot of those details and adds new ones, making it relatievly easy to
implement.

Understanding the relationship between IndieAuth and OAuth 2 requires a fair
bit of knowledge about how OAuth 2 operates.  Fortunately, you don't need to
know any of this if all you want to do is sign in to an IndieAuth enabled
service using your domain.  Read on for information on how to do that.

## For the Impatient

If you already have a social media profile and a personal website you can
enable IndieAuth on your domain *right now*.  Let's use Github as an
example.

First, add a special "me" anchor tag to your home page detailing where to
find the profile you want to use for authentication purposes:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it like any other link on your home page.

Next, in your Github profile, you need to make sure you include a link back
to your domain, to show that you actually control that account.  A "me" link
is not valid (with respect to the IndieAuth protocol) unless it points to a
profile that points back to your homepage.

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

## For the Less Impatient
