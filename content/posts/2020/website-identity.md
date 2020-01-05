title: Website and Identity
date: 2019-12-15 16:30:11
modified: 2019-12-15 16:30:11
status: draft


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
