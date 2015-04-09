from __future__ import unicode_literals
import datetime

# General settings
AUTHOR = 'Florian M. Wagner'
SITENAME = 'Florian M. Wagner'
SITEURL = ''

# Path settings
DELETE_OUTPUT_DIRECTORY = True
PATH = 'content'
STATIC_PATHS = ['static']
TIMEZONE = 'Europe/Paris'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL
DIRECT_TEMPLATES = ()

DEFAULT_LANG = 'en'

MENUITEMS = (('About me', 'index.html'),
         ('Curriculum Vitae', 'cv.html'),
         ('Publications', 'publications.html'),
         ('Contact', 'contact.html'),
         )

PLUGINS = ['pelican_fontawesome']

# Social widget
SOCIAL = (
    ('envelope-o', 'mailto:mail@fwagner.info'),
    ('google', 'http://scholar.google.de/citations?user=mi_Wm7kAAAAJ'),
    ('graduation-cap', 'http://www.researchgate.net/profile/Florian_Wagner5'),
    ('linkedin', 'https://www.linkedin.com/pub/florian-wagner/43/838/970'),
    ('xing', 'https://www.xing.com/profile/FlorianM_Wagner'),
    ('github', 'https://github.com/florian-wagner')
)

DEFAULT_PAGINATION = False

# For modification date in footer
TODAY = datetime.date.today().isoformat()

# Theme settings
THEME = 'themes/pure-single'
PROFILE_IMG_URL = '/static/fwagner.jpg'
COVER_IMG_URL = '/static/bg.jpg'
TAGLINE = "Geophysicist / Data Scientist"
