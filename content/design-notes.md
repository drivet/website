date: 2012-07-12 01:44:03
modified: 2015-05-16 01:52:55.879342
title: Site Design and Layout

At the moment, this site is mostly an experiment in python.  The pages and
the blog are all delivered via a home-grown blogging system/CMS that I've
called [YAWT][1] (Yet Another Weblog Tool), written in python.  It's a work
in progress.  At some point, I intend to write a page about it.

As a rule, I like to have control over the HTML that gets put on my site.
Writing simple, standards compliant and semantically sound HTML has always
been important to me.  In the past, this meant making sure my site was HTML
4 or XHTML 1.0 compliant, and preferring semantic tags over non-semantic
tags (i.e. prefering "em" over "i").  More recently, this has meant making
sure that my site was HTML5 compliant.  Where appropriate, I've made use of
the newer tags such as "header", "footer" and "article" and I've taken
advantage of the newer HTML5 outlining algorithm to embed multiple h1 where
it makes sense.  The whole thing is mostly a tempest in a teapot, but from a
technical standpoint it soothes my soul to know I've done what I can in this
area.

For the most part, the stuff on this site should look okay in older and text
based browsers, as long as you turn off the CSS.  As I have no sense of
aesthetics, I've used [twitter bootstrap 3][2] as a starting point for the
styling.  I've avoided javascript where I could, though it's still used for
the responsive features.

This site consists of standalone pages, like this one, and a [blog][3] which
publishes random thoughts on a semi-regular basis.

The search bar at the top will search the whole site, which for now just
means my blog and standalone pages. I have very vague plans to implement a
photo gallery engine, and if that ever takes shape, I'm hoping the search
bar will included the photos as well.

[1]: https://github.com/drivet/yawt
[2]: http://twitter.github.com/bootstrap/
[3]: /blog