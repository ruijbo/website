from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import roles

def icon(name, rawtext, text, lineno, inliner, options={}, content=[]):
    html = '<i class="icon-%s"></i>' % text
    return [nodes.raw('', html, format='html')], []


def register():
    roles.register_local_role('icon', icon)
