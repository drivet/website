#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://desmondrivet.com'
RELATIVE_URLS = False

DRAFT_URL = ''
DRAFT_SAVE_AS = ''

# plugins are the same as non-publish mode, but had bridgy enabled for syndication
PLUGINS = ['subcategory', 'tipue_search', 'i18n_subsites',
           'pelican_notedown', 'paragraphed-summary', 'pelican_webmention']
