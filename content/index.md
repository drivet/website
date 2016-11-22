---
title: Welcome to the Low Rent District
---

Hi everyone. You've reached the personal domain of Desmond Rivet.  There
have been a few over the years but I'm going to try and make this one last.

<div class="faqtitle" markdown="1">
## Infrequently Asked Questions
</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> Who are you?

I'm a software developer living in Montreal, Quebec.  I've written up some
[personal information][1] if you're interested.
</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> Why "The Low Rent District"?

This site is called "The Low Rent District" because:

 * I live in Saint-Henri, a neigbourhood of Montreal which is generally
   considered to be low-rent.
 * When it comes to technology, I tend to be cheap.
</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> What kind of stuff do you have on here?

At the moment this domain is home to a [wiki][2], and a [blog][3], mostly
for whatever musings du jour I feel the need to get off my chest. Feel free
to peruse them both.  I've also written up some [personal information][1]
and [site design notes][4] if you're interested.

Before I started maintaining blog, I used to just write random, ad-hoc
essays and pages.  I've [indexed most of these][6] elsewhere on my site.

</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> A wiki?  What is this, 2005?

I have been informed on a couple of occasions that wikis are dated, and that
I should be using Google Docs instead.

I respectfully disagree.  I find that Google Docs works too much like
Microsoft Word, which I don't find pleasant to use.  I'm sure that was the
whole point, and the Google Docs team did a great job in this respect, but
that doesn't mean I like it any better.

When I write anything longer than a couple of sentences, I like using
Markdown.  If that's not available, then I like using some form of wiki
markup.  The main point here is that I like writing things in plain text.
It's more portable and it lasts longer.
</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> Why is your wiki domain password protected?

I found that too many people were trying to edit and create new accounts on
the wiki, which was hogging alot of resources on my relatively low end VPS.
Rather than turning off the feature, I just password protected the areas in
question, and whitelisted the IP addresses from which I usually access the
wiki.  This seems to work, and everything seems to be alot faster, but I'm a
little sad that I had to take this step.
</div>

<div class="question" markdown="1">
### <span class="fa fa-caret-right"></span> Why do I get a security warning when I try to access your wiki?

The entire wiki domain, in addition to being password procted, is also
protected with an SSL certificate, so that I can log into the wiki using a
plain password without worrying too much about people snooping.  

It ended up being easier to protect the whole domain rather than trying to
just protect the login stage, which basically means that you need to use
HTTPS even if you just want to read the wiki.

You have two options if you want to access the wiki:

 * Live with the warning your browser gives you
 * Download and install my [personal root certificate][5]
</div>


[1]: aboutme.html
[2]: http://wiki.desmondrivet.com
[3]: /blog
[4]: design-notes.html
[5]: /static/desmond_rivet_intl_ca.crt
[6]: /oldsite