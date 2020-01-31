title: Your Website is Your Passport
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft

One of the themes that crops up again and again in the IndieWeb community is
that your personal domain, with a website attached to it, should form the
nexus of your online existence.  On the IndieWeb, even if you *also* spread
yourself across a multitude of different social media sites, these profiles
nonetheless remain subordinate to your personal website, the central hub out
of which your other identities radiate, and everyone's one-stop-shop for
everything *you* related.

Part of what this means in practice is that you should be able to use your
domain as a kind of universal online identifier or passport so that you can
sign in to services and applications which support it.  We've all seen
applications with "Sign in with Facebook" and "Sign in with Google" buttons.
The idea is to be able to do the same thing with your personal URL.

How is this accomplished?  There is a short answer and there is a long
answer.

## For the Impatient

If you have a social media profile and a website (even a simple "Hello
World!" one will suffice) on a domain that you control, you can use that
domain to sign in to a service like indieweb.org by following a few simple
steps.

First, add a special "me" anchor tag to your home page detailing where to
find the profile you want to use for authentication purposes:

    <a href="https://github.com/drivet" rel="me">Github</a>

Note that there is nothing special about this link, aside from the "me"
attribute.  You can use it like any other link on your home page.

Next, edit your Github profile so that the Website field points back to your
domain.  You do this to show that you actually control the Github account to
which your homepage is pointing.

Finally, you add this link tag to the head of your home page:

    <head>
        ....
        <link rel="authorization_endpoint" href="https://indieauth.com/auth">
    </head>

You should now be able to sign in to, for example, indieweb.org.  You can
try it now by going to the site and clicking the "Log in" link.

You'll be presented with a text box into which you can enter you personal
domain. The service will look for an authorization_endpoint link in your
homepage, and will delegate the authentication procedure to the first "me"
link it finds.  Obviously, if you use this procedure, you are still
dependant on an external social networking profile for authentication
purposes, which is less than ideal, but at least the process starts with
your own domain, and there are ways to detach yourself from your external
profiles completely if you wish to go that far.

## For the Less Impatient

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
