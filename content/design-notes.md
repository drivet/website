date: 2012-07-12 01:44:03
modified: 2015-05-16 01:52:55.879342
title: Site Design and Layout

In the past, this website was diven by homemade blogging engine called
[YAWT][1].  It worked fairly well, but I eventually got tired of maintaining
it, so I switched to a static site generator called [pelican][4].  Like
YAWT, it's written in python and uses the [Jinja2][5] tempating system, so I
didn't feel completely out of place.

As a rule, I like to have control over the HTML that gets put on my site.
Writing simple, standards compliant and semantically sound HTML has always
been important to me.  In the past, this meant making sure my site was HTML
4 or XHTML 1.0 compliant, and preferring semantic tags over non-semantic
tags (i.e. prefering "em" over "i").  More recently, this has meant making
sure that my site was HTML5 compliant.  Where appropriate, I've made use of
the newer tags such as "header", "footer" and "article" and I've taken
advantage of the newer HTML5 outlining algorithm to embed multiple h1 tags
where appropriate.

For the most part, the stuff on this site should look okay in older and text
based browsers, as long as you turn off the CSS.  I've based the look of the
site off of a somewhat tweaked version of the [pelican-boostrap3][2] theme.

This site consists of standalone pages, like this one, and a [blog][3] which
publishes random thoughts on a semi-regular basis.  I have hopes of
incorporating a simple wiki using pelican as well, but until that happens, I
run a [separate one][6].  Before I started blogging, I also used to write
random, ad-hoc essays and pages, which I've [indexed][7] elsewhere on my
site if you're interested.

[1]: https://github.com/drivet/yawt
[2]: https://github.com/DandyDev/pelican-bootstrap3
[3]: /blog
[4]: http://blog.getpelican.com/
[5]: http://jinja.pocoo.org/docs/dev/
[6]: http://wiki.desmondrivet.com
[7]: /oldsite
