Title: The Use Case for OAuth
Status: draft

You have a Twitter account, with a feed of tweets.

You also maintain a blog.  You'd like to show the latest 5 tweets from your
feed on the front page of your blog.

Twitter provides a REST API for exactly this purpose.  But you don't want
just anyone to have access to your tweets.  So how do you secure it?

In the past, a problem like this may have been solved by coding your
credentials (username, password) in your blogging application, so that it
could pass them to the Twitter API, thus allowing access to your feed.
This, obviously, has various problems:

* Your password is configured somewhere, probably in plaintext.
* There is no discrimination between resources.  Maybe you're okay with
  giving read access to your feed, but you don't want people to have write
  access to your feed - and you certainly don't want anyone to have read
  access to your direct messages.
* What if you want to revoke access?

OAuth is meant to help with these problems.
