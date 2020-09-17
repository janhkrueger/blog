#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Generelle Blogeinstellungen
AUTHOR = u'Jan H. Krueger'
SITENAME = u'JHK Blog'
SITEURL = 'https://janhkrueger.de/blog/'
SITESUBTITLE = 'Das private Blog von Jan H. Krueger'
TIMEZONE = 'Europe/Berlin'

DEFAULT_CATEGORY = 'Allgemein'
USE_FOLDER_AS_CATEGORY=True

PATH = 'content'
OUTPUT_PATH = 'public'

# global metadata to all the contents
DEFAULT_METADATA = (('jhk', 'blog'),)


DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll, Links im Seitenmenue
LINKS=(
    ('Piratenpartei','https://piratenpartei.de'),
    ('Free Software Foundation Europe','https://fsfe.org'),
    ('The game without name','http://tgwnn.rpgame.de/'),)

# Social widget
# Nur ein direkter Zugriff auf die RSS-Feeds
SOCIAL = (
    ('Twitter', 'https://twitter.com/janhkrueger'), 
    ('gitlab', 'https://gitlab.com/janhkrueger'),
    ('RSS', 'https://janhkrueger.de/blog/feeds/all.rss.xml'),)

# Twitter
TWITTER_USERNAME='janhkrueger'
TWITTER_CARDS=True

DEFAULT_PAGINATION = 5

# Lizenz unter welcher das Blog betrieben wird
CC_LICENSE = 'CC-BY-NC-SA'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
