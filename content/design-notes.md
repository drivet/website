date: 2012-07-12 01:44:03
modified: 2015-05-16 01:52:55.879342
title: Design Notes

I've maintained some form of personal website since roughly 1998 or so, when
I made my first hand coded HTML pages available online.  There've been a few
over the years, hosted on variously on [U of T][8] servers, [Geocities][9],
[Netfirms][10] and a raft of dedicated home machines, but the current
incarnation has lived on a server rented from [kimsufi][11] for some time
now and I'm trying to make it last.

## Tools

I use a static site generator (SSG) called [pelican][4].  In the past, I
used a homemade blogging engine called [YAWT][1] (written in perl, then
python).  which worked fairly well, but I eventually got tired of
maintaining it, so I switched.  Like YAWT, pelican is written in python
and uses the [Jinja2][5] templating system, so I didn't feel completely out
of place.

Using an SSG means compiling the HTML pages comprising this site every time
new content gets added.  I keep the website source files in my [github
repo][12] and I compile and deploy the site with every push.

The look of the site is based off of [my own pelican theme][13], which uses
[bootstrap][14] to do most of the heavy lifting.  I've tried to make the
site HTML5 compliant and, as such, I've made use of the newer tags such as
"header", "footer" and "article" and I've taken advantage of the newer HTML5
outlining algorithm to embed multiple h1 tags where appropriate.  For the
most part, the stuff on this site should look okay in older and text based
browsers, as long as you turn off the CSS.

## Indie Web

I discovered the [Indie Web][15] community sometime in early 2019 and I've
been slowly trying to make my site compliant.  So far I'm only at
[IndieMark][16] Level 1, which basically means that I own a domain, post
some original content ([blog entries][3] and [notes][17]), and can use my
website as a means of authentication.  I'm hard at work on Level 2.


[1]: https://github.com/drivet/yawt
[3]: /blog
[4]: http://blog.getpelican.com/
[5]: http://jinja.pocoo.org/docs/dev/
[8]: https://www.utoronto.ca/
[9]: https://en.wikipedia.org/wiki/Yahoo!_GeoCities
[10]: https://www.netfirms.ca/
[11]: https://www.kimsufi.com/ca/en/
[12]: https://github.com/drivet/website
[13]: https://github.com/drivet/pelican-indieweb
[14]: https://getbootstrap.com
[15]: https://indieweb.org/
[16]: https://indieweb.org/IndieMark
[17]: /notes
