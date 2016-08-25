from __future__ import unicode_literals
import datetime
import os

# General settings
AUTHOR = 'Florian M. Wagner'
SITENAME = AUTHOR

if "TRAVIS" in os.environ:
    SITEURL = 'http://www.fwagner.info'
else:
    SITEURL = 'http://localhost:8000'

# Path settings
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['static', 'paper', 'javascript']
TIMEZONE = 'Europe/Paris'
SLUGIFY_SOURCE = 'basename'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
DIRECT_TEMPLATES = ()
ARTICLE_EXCLUDES = ['javascript']

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_LANG = 'en'

MENUITEMS = (('About', ''),
         ('Curriculum Vitae', 'cv'),
         ('Dissertation', 'thesis'),
         ('Publications', 'publications'),
         ('Contact', 'contact'),
         )

PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_fontawesome', 'html_rst_directive']

# Social widget
SOCIAL = (
    ('ai ai-google-scholar ai-2x', 'http://scholar.google.de/citations?user=mi_Wm7kAAAAJ'),
    ('ai ai-researchgate ai-2x', 'http://www.researchgate.net/profile/Florian_Wagner5'),
    ('ai ai-orcid ai-2x', 'http://orcid.org/0000-0001-7407-9741'),
    ('fa fa-linkedin fa-2x', 'https://www.linkedin.com/in/fmwagner'),
    ('fa fa-xing fa-2x', 'https://www.xing.com/profile/FlorianM_Wagner'),
    ('fa fa-github fa-2x', 'https://github.com/florian-wagner')
)

DEFAULT_PAGINATION = False

# For modification date in footer
TODAY = datetime.date.today().isoformat()
DEFAULT_DATE = 'fs'

# Theme settings
THEME = 'themes/pure-single'
PROFILE_IMG_URL = '/static/fwagner.jpg'
COVER_IMG_URL = '/static/bg.jpg'
TAGLINE = 'Geophysicist / Data Scientist'
