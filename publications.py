#!/usr/bin/env python
# encoding: utf-8

"""
File: publications.py
Author: Florian Wagner <fwagner@gfz-potsdam.de>
Description: Create RST reference list from bibtex file.
Created on: 2015-01-17
"""

from __future__ import print_function
from bibtexparser import load
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import re

from collections import defaultdict

import re
gimli = re.compile(re.escape('pygimli'), re.IGNORECASE)

def parse_bib(fname):
    """ Read bibtex file and sort by year. """

    with open(fname) as bibfile:
        parser = BibTexParser()
        parser.customization = convert_to_unicode
        bp = load(bibfile, parser=parser)
        references = bp.get_entry_list()

    references.sort(key=lambda x: x['year'], reverse=True)
    refs = defaultdict(list)

    for r in references:
        refs[r['year']].append(r)

    refsbyyear = []
    for year in refs.keys():
        refsbyyear.append((year,refs[year]))
    refsbyyear.sort(key=lambda x: x[0], reverse=True)

    return refsbyyear

def write_entry(entry, fhandle):
    """ Write beginning on entry. """

    #print(entry)
    fhandle.write("  ")
    if "and" in entry["author"]:
        authors = entry["author"].split("and")
        ands = True
    else:
        authors = entry["author"].split(',')
        ands = False

    for i, author in enumerate(authors):
        if ands:
            name = [n.strip() for n in author.split(",")]
        else:
            name = [n.strip() for n in reversed(author.split())]

        if "Wagner" in name:
            fhandle.write("**%s %s**" % ("F\. M\.", name[0]))
        else:
            fhandle.write("%s %s" % (name[1][0] + "\.", name[0]))
        if i < len(authors) - 1:
            fhandle.write(", ")
        else:
            fhandle.write(" (" + entry["year"] + "): ")

    title = entry["title"].replace("CO2", "CO\ :sub:`2`\ ")
    title = gimli.sub('`pyGIMLi\ <http://www.pygimli.org/>`_', title)

    fhandle.write(title + ". ")

articles = parse_bib("content/articles.bib")
conference = parse_bib("content/conference.bib")

f = open("./content/pages/publications.rst", "w")

f.write("""
.. role:: raw-html(raw)
   :format: html

""")

pdf = " :raw-html:`<a target=\"_blank\" href=\"%s\"><i class=\"fa fa-file-pdf-o\"></i></a>`"
#citations = " :raw-html:`<object height=\"50\" data=\"http://api.elsevier.com/content/abstract/citation-count?doi=%s&httpAccept=text/html&apiKey=557b7437b48874840f9cb4d8b0650079\"></object>`"

f.write("""
Publications
============
:class: test

Journal articles
----------------
""")

for year in articles:
    f.write(year[0] + "\n")
    f.write("^^^^\n\n")

    for article in year[1]:
        write_entry(article, f)
        f.write("*" + article["journal"] + "*, ")
        f.write(article["volume"] + ", ")
        f.write(article["pages"] + ", ")
        if len(article["doi"]) > 3:
            f.write("http://dx.doi.org/" + article["doi"] + ".")
        if "link" in article and len(article["link"]) > 10:
            f.write(pdf % article["link"])
        #if len(article["doi"]) > 3:
            #f.write(citations % article["doi"])
        f.write("\n\n")

f.write("Conference contributions\n")
f.write("------------------------\n\n")

for year in conference:
    f.write(year[0] + "\n")
    f.write("^^^^\n\n")

    for article in year[1]:
        write_entry(article, f)
        if 'booktitle' in article:
            f.write("*" + article["booktitle"] + "*")
        elif 'series' in article:
            f.write("*" + article["series"] + "*")
        else:
            f.write("*Conference Proceeding*")
        if 'doi' in article:
            f.write(", http://dx.doi.org/" + article["doi"])
        f.write('.\n\n')
        if "link" in article and len(article["link"]) > 10:
            f.write(pdf % article["link"])
f.close()
