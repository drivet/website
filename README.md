# website
My personal website and blog.

Pelican is, currently, my blogging tool of choice.  I have the following
third-party plugins enabled:

* tipue_search

And I have the following homegrown plugins enabled as well:

* [paragraphed-summary][https://github.com/drivet/paragraphed-summary]
* [pelican-cool-uri][https://github.com/drivet/pelican-cool-uri]

To browse a local copy, you'll need a pelican virtualenv set up with pelican
and its dependencies installed.  The plugins are handled separately.  You
need to make sure you have the plugins cloned from github somewhere on your
drive and you need to point pelican at them via its configuration file.

Generating the website locally is done with this command:

```
pelican content/ -o output/
```

And if you're generating for publication, run this:

```
pelican -s publishconf.py content/ -o output_p/
```

Then rsync the output over to the remote server.
