title: In the Beginning was the Website: On Joining the IndieWeb
date: 2019-01-20 20:50:28
modified: 2019-01-20 20:50:28
status: draft

I don't think I've ever felt quite as old as I felt when, last year, I
discovered the [IndieWeb][5], an online community dedicated to resuscitating
the personal website.

This makes me feel old because I've maintained some sort of personal web
presence/site/blog since about 1998 or so, when I made my first hand-coded
HTML pages available online at U of T, and apparently enough time has past
not *only* for the concept of a "personal website" to have become quaint and
old-fashioned but *also* for it to have been re-energized by an enthusiastic
band of hobbyists with a taste for the retro and a fondness for old-school
fan pages.

You hear that?  I've moved beyond passé into *retro*.  It's as if I never
stopped wearing 80's clothes but now they're cool again so it's okay.

## Why Not the Status Quo?

To be honest, until I stumbled upon the IndieWeb, it had never even occurred
to me that the personal website was a thing that needed reviving but, in
retrospect, it does seem obvious that I'm a bit of an outlier.  Personal
blogs (in the sense of someone running their own blogging software on their
own domain) are not something you see much nowadays; people with something
pithy to say will use Twitter or Facebook and those with longer attention
spans will use something like Medium.  It's just easier, right?

Why would anyone want something different?  The answer could probably be
summarized in one word: control.

When you post a tweet, it's no longer yours; it becomes the property of
Twitter and they can do what they like with it.  What happens to your tweets
or status updates if Twitter or Facebook go out of business?  It seems
unlikely, but times change.

Or, perhaps more likely, what happens if you simply want to leave? Imagine
that Facebook crosses one too many lines and you decide that you're better
off without it.  What happens to your content then?

What happens if Medium decides to start charging money and you decide it's
not worth it?

I mean, sure, there are other reasons to avoid these sites.  No one likes to
see ads.  Facebook is constantly tracking your online activities and selling
what it collects to nefarious organizations.  Twitter contributes to the
echo chamber effect.

But honestly? These all take a back seat to the issue of control.  Even if
there existed a completely benign, free, adless, non-tracking social
network, the problems I described would still exist.

## Failed Attempts

There have been attempts over the years to push sites like Facebook off
their perch.  They all failed for various reasons.

One of the first and most notable ones was [Diaspora][6].  It was touted as a
kind of decentralized Facebook, where users could post status updates and
pictures, send messages, etc.  Users joined Diaspora by hosting their own
"pod", running specialized software, which would communicate with other pods
in the Diaspora network.  There was also a hosted version that you could
sign up for, but that kind of defeated the purpose of the whole endeavour.

It was an interesting experiment, but it failed miserably.  Many people
point to the fact that the initial software offering was riddled with bugs,
and that setting up your own pod was a daunting task, but in reality I think
the reason was simpler: Disapora ultimately didn't have very many users.
Imagine going to all the trouble to launch a Disapora pod only to discover
that no one you knew was on the network?

More subtly, the issue is also one of interoperability.  The IndieWeb
community's blanket term for sites like Facebook and Twitter is "silos" and
the metaphor is apt.  People take it for granted that Facebook users don't
get to follow you on Twitter unless they're also Twitter users.  Sending a
message to someone on Facebook doesn't work unless that person is also a
Facebook user.  You don't get to comment on Medium articles unless you
create yourself a Medium account.

Despite being decentralized and free, Diaspora is also a kind of silo.
Generally speaking, when you post something to Diaspora, the only people who
can see it are other Disapora users.  Your posts do not show up, for
example, on someone's Twitter feed.

Can you imagine if something as basic as email worked like that?  Can you
imagine if Gmail users were restricted to sending emails to other Gmail
users?  The fact that they are not so restricted is directly attributed to
the fact that the protocols involved in sending emails are open standards.
Even if you opt for a Gmail account, with your emails ultimately under
Google's control, the idea that you couldn't use that account to send emails
to someone who uses, say, [ProtonMail][7], is absurd.

So...why can't social networking work like that?  Good question.

## Enter the IndieWeb

The IndieWeb is an attempt to bring the benefits of social networking, such
as posting and sharing status updates, likes and reposts, to the web at
large, using open protocols.  Whereas a site like Twitter or Facebook is a
kind of walled garden, with online social interactions restricted to the
confines of the site, the IndieWeb tries to create a social network *out of
the world wide web itself*.

The Diaspora project, of course, tried to do the same thing, more or less,
with its vision of a social network consisting of a decentralized collection
of web "pods" communicating among themselves via the Diaspora software
suite.  As noted, it failed because, at the end of the day, it tried to be
an out-and-out replacement for Facebook, which was an unrealistic goal -
Facebook has billions of users, and they aren't budging anytime soon.

The IndieWeb is a somewhat different beast.  You don't need to run a
specialized "pod" to become part of the IndieWeb.  You just need a standard,
vanilla personal website - albeit one that conforms to certain
(straightforward) patterns.  After that, sharing a status update consists of
posting content to your own site, where anyone can read it, using whatever
mechanism is most convenient for you.

This is an important point to grasp, so I'll reiterate.  A personal website
belonging to the IndieWeb isn't running any particular suite of software.
It's a standard website, written with standard HTML and CSS.

One of the key differences between the IndieWeb and similar projects like
Disapora is that the former prescribes a methodology or pattern for
[syndicating your content to sites like Twitter][8] and for [harvesting
online interactions to those syndicated copies][9] for use on your own site.
In other words, the IndieWeb is not trying to dislodge the existing social
networking giants, but is rather trying to cooperate with them.  This is a
crucial feature, and is the main reason why adoption numbers don't really
matter as much to the IndieWeb as they did to other attempts at open social
networking.  Even if the entire IndieWeb consisted of a single personal
website, it would still "work", in the sense that the owner of the website
would be in control of their own content and would still be able to share
that content with their friends on (say) Twitter.


[1]: https://en.wikipedia.org/wiki/Randall_Munroe
[2]: https://www.xkcd.com/
[3]: https://imgs.xkcd.com/comics/the_simpsons.png 
[4]: https://imgs.xkcd.com/comics/movie_ages.png 
[5]: https://indieweb.org/
[6]: https://diasporafoundation.org/
[7]: https://protonmail.com/
[8]: https://indieweb.org/POSSE
[9]: https://indieweb.org/backfeed
