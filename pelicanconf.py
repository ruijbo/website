#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General settings
AUTHOR = 'Florian M. Wagner'
SITENAME = 'Florian M. Wagner'
SITEURL = '/'

# Path settings
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['img', 'html']
TIMEZONE = 'Europe/Paris'
INDEX_SAVE_AS = 'blog.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

DEFAULT_LANG = 'en'

MENUITEMS = (('About me', 'index.html'),
         ('Curriculum Vitae', 'cv.html'),
         ('Publications', 'publications.html'),
         #('Contact', 'contact.html'),
         )

# Social widget
SOCIAL = (
    ('envelope-o', 'mailto:mail@fwagner.info'),
    ('google', 'http://scholar.google.de/citations?user=mi_Wm7kAAAAJ'),
    ('graduation-cap', 'http://www.researchgate.net/profile/Florian_Wagner5'),
    ('linkedin', 'https://www.linkedin.com/pub/florian-wagner/43/838/970'),
    ('xing', 'https://www.xing.com/profile/Florian_Wagner92'),
    ('github', 'https://github.com/florian-wagner')
)

DEFAULT_PAGINATION = False

THEME = 'themes/pure-single'
PROFILE_IMG_URL = '/img/fwagner.jpg'
COVER_IMG_URL = '/img/bg.jpg'
TAGLINE = "Geophysicist / Data Scientist"
