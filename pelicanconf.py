#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Desmond Rivet'
# AUTHOR_OG = 'https://www.facebook.com/desmond.rivet'
# most themes expect the SITENAME to be the blog name
SITENAME = 'Desmond Rivet'
BLOGNAME = 'Lifestream'
SITEURL = ''

DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'

THEME = '/home/dcr/repos/pelican-indieweb-kit/theme'
#THEME_TEMPLATES_OVERRIDES = ['templates']

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %b, %Y %-I:%M %p'

# Syndication
FEED_DOMAIN = SITEURL
FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss'
SUBCATEGORY_FEED_RSS = 'feeds/%s.rss'

CATEGORY_FEED_ATOM = None
FEED_ALL_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
SUBCATEGORY_FEED_ATOM = None

# Social widget
SOCIAL = (('Facebook', 'http://www.facebook.com/desmond.rivet', 'fab fa-facebook-square'),
          ('Instagram', 'https://www.instagram.com/thegreatdesmondo/', 'fab fa-instagram'),
          ('Twitter', 'http://www.twitter.com/desmondrivet', 'fab fa-twitter'),
          ('Github', 'https://github.com/drivet', 'fab fa-github fa-lg'),
          ('LinkedIn', 'http://ca.linkedin.com/in/desmondrivet', 'fab fa-linkedin-in'))

FAVICON = 'me_200x200.jpg'

# Links for the nav bar
MENUITEMS = (('Lifestream', '/all'),
             ('Notes', '/notes'),
             ('Blog', '/blog'),
             ('Photos', 'https://photos.desmondrivet.com'),
             ('Wiki', 'https://wiki.desmondrivet.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['/home/dcr/repos',
                '/home/dcr/repos/pelican-plugins',
                '/home/dcr/PycharmProjects',
                '/home/dcr/repos/pelican-indieweb-kit']
PLUGINS = ['subcategory', 'tipue_search', 'i18n_subsites', 'pelican_notedown',
           'paragraphed-summary', 'pelican_webmention']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

USE_FOLDER_AS_CATEGORY = True

# I'm the only author, so don't save these
AUTHORS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# each entry in this list has a corresponding "direct" template in the theme
DIRECT_TEMPLATES = ['index', 'categories', 'archives', 'tags', 'search']

ARCHIVES_SAVE_AS = 'archives.html'
ARCHIVES_URL = 'archives'
CATEGORIES_SAVE_AS = 'categories.html'
CATEGORIES_URL = 'categories'
TAGS_SAVE_AS = 'tags.html'
TAGS_URL = 'tags'
INDEX_SAVE_AS = 'all.html'
INDEX_URL = 'all'

PAGE_PATHS = ['']
ARTICLE_PATHS = ['blog', 'notes']
STATIC_PATHS = ['']

TWITTER_LINK = 'https://twitter.com/desmondrivet/status/{twitterid}'
TWITTER_HASHTAG = 'https://twitter.com/hashtag/{hashtag}'

PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
    'period_archives': None
}

# slug for article comes from base filename
SLUGIFY_SOURCE = 'basefile'

FILENAME_METADATA = '(?P<slug>.*)'
PATH_METADATA = '(?P<path_no_ext>((?P<subcategory_path>.*)/.*)|(.*))\..*'

# this more or less implements my favored permalink scheme
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'


YEAR_ARCHIVE_URL = '{date:%Y}/'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

MONTH_ARCHIVE_URL = '{date:%Y}/{date:%m}/'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DAY_ARCHIVE_URL = '{date:%Y}/{date:%m}/{date:%d}/'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
SUBCATEGORY_SAVE_AS = '{savepath}.html'
SUBCATEGORY_URL = '{fullurl}'

TAG_URL = 'tags/{slug}'
TAG_SAVE_AS = 'tags/{slug}.html'

PAGE_URL = '{path_no_ext}'
PAGE_SAVE_AS = '{path_no_ext}.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

SUMMARY_MAX_LENGTH = 100

# theme options
CUSTOM_CSS = 'static/custom.css'
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_BREADCRUMBS = False

OPEN_GRAPH_IMAGE = 'me_200x200.jpg'

GA_TRACKING_ID = 'UA-132755534-1'

# h-card info
H_CARD_NICKNAME = "desmondrivet"
H_CARD_EMAIL = "desmond.rivet@gmail.com"
H_CARD_URL = SITEURL
H_CARD_PHOTO = "/me01.jpg"

NOTEDOWN_HASHTAG_TEMPLATE = r'https://twitter.com/hashtag/{hashtag}'
NOTEDOWN_MENTION_TEMPLATE = r'https://twitter.com/{mention}'

# root URL where you go to edit content files on the web
#
EDIT_ROOT=r'https://github.com/drivet/website/edit/master/'+PATH

AUTH_ENDPOINT = r'https://desmondrivet.com/auth/'
TOKEN_ENDPOINT = r'https://tokens.indieauth.com/token'
MICROPUB_ENDPOINT = r'https://desmondrivet.com/micropub'
WEBMENTION_ENDPOINT = r'https://desmondrivet.com/webmention'


# webmention folder relative to content
WEBMENTION_PATH = 'webmentions'

WEBMENTION_FROM_DATE = '2019-05-10T12:00:00'
WEBMENTIONS_CACHE_FILE = 'state/webmentions_cache.yml'
WEBSITE_GITHUB_CONTENTS_URL = 'https://api.github.com/repos/drivet/website/contents'

BRIDGY_MP_SYNDICATE_TO_MATCH = {
    '^twitter_bridgy_no_link$': 'https://brid.gy/publish/twitter?bridgy_omit_link=true',
    '^twitter_bridgy$': 'https://brid.gy/publish/twitter',
}

BRIDGY_LIKE_OF_MATCH = {
    'https://twitter.com/(.*)': 'https://brid.gy/publish/twitter',
}

BRIDGY_REPOST_OF_MATCH = {
    'https://twitter.com/(.*)': 'https://brid.gy/publish/twitter?bridgy_omit_link=true',
}

BRIDGY_IN_REPLY_TO_MATCH = {
    'https://twitter.com/(.*)': 'https://brid.gy/publish/twitter?bridgy_omit_link=true',
}

BRIDGY_SYNDICATED_LOCATIONS = ['https://twitter.com/(.*)']

WEBMENTIONS_CACHE_FILE = 'state/webmention_cache.yml'
WEBMENTIONS_CONTENT_HEADERS = ['like_of', 'repost_of', 'in_reply_to']
