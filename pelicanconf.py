from __future__ import unicode_literals
import datetime
import os
import subprocess

# General settings
AUTHOR = 'Florian M. Wagner'
SITENAME = AUTHOR
SRCURL = 'https://github.com/florian-wagner/website'

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
PLUGINS = ['html_rst_directive', 'icons']

# Social widget
SOCIAL = (
    ('google-scholar', 'http://scholar.google.de/citations?user=mi_Wm7kAAAAJ'),
    ('researchgate', 'http://www.researchgate.net/profile/Florian_Wagner5'),
    ('orcid', 'http://orcid.org/0000-0001-7407-9741'),
    ('linkedin', 'https://www.linkedin.com/in/fmwagner'),
    ('xing', 'https://www.xing.com/profile/FlorianM_Wagner'),
    ('github', 'https://github.com/florian-wagner')
)

DEFAULT_PAGINATION = False

# Get the current git commit hash
COMMIT = ''
process = subprocess.Popen('git rev-parse HEAD'.split(), cwd='.',
                           stdout=subprocess.PIPE)
git_hash = process.communicate()[0].strip().decode('utf-8')
if git_hash:
    COMMIT = "{url}/commit/{commit}".format(
    url=SRCURL, commit=git_hash, commit_link=git_hash)

# For modification date in footer
TODAY = datetime.date.today().isoformat()
DEFAULT_DATE = 'fs'

# Theme settings
THEME = 'themes/pure-single'
PROFILE_IMG_URL = '/static/fwagner.jpg'
COVER_IMG_URL = '/static/bg.jpg'
TAGLINE = 'Geophysicist / Data Scientist'
