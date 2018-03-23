#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# DCR - additional config to define the parent site
PARENT_SITENAME = 'The Low Rent District'

AUTHOR = 'Desmond Rivet'
#AUTHOR_OG = 'https://www.facebook.com/desmond.rivet'

# most themes expect the SITENAME to be the blog name
SITENAME = 'The Soapbox'
SITESUBTITLE = 'Random Musings in Blog Form'
SITEURL = ''

DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'

THEME = 'themes/pelican-website'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

# Syndication
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'blog/feeds/all.atom.xml'
FEED_ALL_RSS = 'blog/feeds/all.rss'
CATEGORY_FEED_ATOM = 'blog/feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'blog/feeds/%s.rss'

TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# No blogroll
LINKS = ()

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/desmond.rivet'),
          ('Twitter', 'http://www.twitter.com/desmondrivet'),
          ('Google+', 'https://plus.google.com/u/0/117299838889583871071'),
          ('Github', 'https://github.com/drivet'),
          ('LinkedIn', 'http://ca.linkedin.com/in/desmondrive'))

# DCR added this
# Links for the nav bar
MENUITEMS = (('About', '/aboutme.html'),
             ('Blog', '/blog'),
             ('Photos', 'https://photos.desmondrivet.com'),
             ('Wiki', 'https://wiki.desmondrivet.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basefile'

FILENAME_METADATA = '(?P<slug>.*)'
PLUGIN_PATHS = ['/home/dcr/repos/', '/home/dcr/blogging/website/plugins']
PLUGINS = ['paragraphed-summary', 'pelican-cool-uri', 'tipue_search']

# I'm the only author
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags', 'search']
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARCHIVES_URL = 'blog/archives.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
CATEGORIES_URL = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'
TAGS_URL = 'blog/tags.html'
INDEX_SAVE_AS = 'blog/index.html'

PAGE_PATHS = ['']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['']

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'

CATEGORY_URL = 'blog/{slug}/index.html'
CATEGORY_SAVE_AS = 'blog/{slug}/index.html'

ARTICLE_URL = 'blog/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{category}/{slug}.html'

TAG_URL = 'blog/tags/{slug}.html'
TAG_SAVE_AS = 'blog/tags/{slug}.html'

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS = '{path_no_ext}.html'
PAGE_URL = '{path_no_ext}.html'

DRAFT_URL = 'blog/drafts/{slug}.html'
DRAFT_SAVE_AS = 'blog/drafts/{slug}.html'


DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

SUMMARY_MAX_LENGTH = 100

# Cool URI path
# For the moment, we only provide Cool URIs for blog entries until I
# figure out what role my stand-alone pages fill in the grand scheme
# of things
COOLURI_PATH = 'blog'

# theme options
CUSTOM_CSS = 'static/custom.css'
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_BREADCRUMBS = False

PIWIK_SITE_ID = 3
PIWIK_URL = 'piwik.desmondrivet.com'
OPEN_GRAPH_IMAGE = 'me_200x200.jpg'

ISSO_SERVER = 'http://isso.desmondrivet.com'
ISSO_DISPLAY_COUNTS = True
