#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Desmond Rivet'
# AUTHOR_OG = 'https://www.facebook.com/desmond.rivet'
# most themes expect the SITENAME to be the blog name
SITENAME = 'Desmond Rivet'
BLOGNAME = 'The Soapbox'
BLOGSUBTITLE = 'Random Musings in Blog Form'
SITEURL = ''

DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'

THEME = '/home/dcr/repos/pelican-website'
#THEME_TEMPLATES_OVERRIDES = ['templates']

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

# Syndication
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'blog/feeds/all.rss'
CATEGORY_FEED_RSS = 'blog/feeds/{slug}.rss'

CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# No blogroll
LINKS = ()

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/desmond.rivet'),
          ('Instagram', 'https://www.instagram.com/thegreatdesmondo/'),
          ('Twitter', 'http://www.twitter.com/desmondrivet'),
          ('Github', 'https://github.com/drivet'),
          ('LinkedIn', 'http://ca.linkedin.com/in/desmondrivet'))

FAVICON = 'me_200x200.jpg'

# DCR added this
# Links for the nav bar
MENUITEMS = (('About site', '/design-notes'),
             ('Blog', '/blog'),
             ('Photos', 'https://photos.desmondrivet.com'),
             ('Wiki', 'https://wiki.desmondrivet.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basefile'

FILENAME_METADATA = '(?P<slug>.*)'
PLUGIN_PATHS = ['/home/dcr/repos', '/home/dcr/repos/pelican-plugins']
PLUGINS = ['paragraphed-summary', 'pelican-cool-uri', 'tipue_search',
           'i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# I'm the only author
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags', 'search']
ARCHIVES_SAVE_AS = 'blog/archives.html'
ARCHIVES_URL = 'blog/archives'
CATEGORIES_SAVE_AS = 'blog/categories.html'
CATEGORIES_URL = 'blog/categories'
TAGS_SAVE_AS = 'blog/tags.html'
TAGS_URL = 'blog/tags'
INDEX_SAVE_AS = 'blog/index.html'

PAGE_PATHS = ['']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['']

YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_URL = 'blog/{date:%Y}/'
MONTH_ARCHIVE_URL = 'blog/{date:%Y}/{date:%m}/'

CATEGORY_URL = 'blog/{slug}/'
CATEGORY_SAVE_AS = 'blog/{slug}/index.html'

ARTICLE_URL = 'blog/{category}/{slug}'
ARTICLE_SAVE_AS = 'blog/{category}/{slug}.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}.html'

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS = '{path_no_ext}.html'
PAGE_URL = '{path_no_ext}'

DRAFT_URL = 'blog/drafts/{slug}'
DRAFT_SAVE_AS = 'blog/drafts/{slug}.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

SUMMARY_MAX_LENGTH = 100

# Cool URI path
# For the moment, we only provide Cool URIs for blog entries until I
# figure out what role my stand-alone pages fill in the grand scheme
# of things
COOLURI_PATH = ''

# theme options
CUSTOM_CSS = 'static/custom.css'
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_BREADCRUMBS = False

#PIWIK_SITE_ID = 3
#PIWIK_URL = 'piwik.desmondrivet.com'
OPEN_GRAPH_IMAGE = 'me_200x200.jpg'

ISSO_SERVER = 'https://isso.desmondrivet.com'
ISSO_DISPLAY_COUNTS = True

GA_TRACKING_ID = 'UA-132755534-1'

# h-card info
H_CARD_NICKNAME = "desmondrivet"
H_CARD_EMAIL = "desmond.rivet@gmail.com"
H_CARD_URL = SITEURL
H_CARD_PHOTO = "/me01.jpg"


