#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Kannan Ramamoorthy'
AUTHOREMAIL = u'kannangce@rediffmail.com'
SITENAME = u'My Thought Buddy'
SITEDESCRIPTION = u'(->> thoughts \n (filter #(curious? %)) \n post-here)'
#SITEURL = 'http://kannangce.in'
#SITEURL = 'http://localhost:8000'
SITEURL = 'https://kannangce.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# THEME = "/Users/kannan.r/Desktop/Kannan/Personal/graymill"
THEME = "../graymill"


# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/kannangce'),
          ('so', 'https://stackexchange.com/users/2333642/kannan?tab=accounts'),
          ('linked-in', 'https://www.linkedin.com/in/kannan-ramamoorthy-54793145/'),
          ('twitter', 'https://twitter.com/kannangce'),
          )

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

PLUGIN_PATHS = (os.path.join(os.path.dirname(__file__), './plugins'),)

ASCIIDOC_CMD = 'asciidoctor'
ASCIIDOC_OPTIONS = []
ASCIIDOC_BACKEND = 'html5'
PLUGINS = [
    "asciidoc_reader.asciidoc_reader",
    "render_asciimath"
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISQUS_SITENAME = "kannangce-in"

GOOGLE_ANALYTICS = "UA-127824340-1"
