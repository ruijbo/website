#!/usr/bin/env python
# encoding: utf-8
"""
File: generate_bib.py
Author: Florian Wagner <mail@fwagner.info>
Description: Create RST reference list from bibtex file.
Created on: 2015-01-17
"""

from __future__ import print_function

import re
from collections import defaultdict
from operator import itemgetter

from bibtexparser import load
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode

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
        yearlist = sorted(refs[year], key=itemgetter("author"), reverse=True)
        sortedlist = []
        for entry in yearlist:
            if entry["author"].startswith("Wagner") or entry["author"].startswith("F. M."):
                sortedlist.insert(0, entry)
            else:
                sortedlist.append(entry)

        refsbyyear.append((year, sortedlist))

    # Newest year first
    refsbyyear.sort(key=lambda x: x[0], reverse=True)

    return refsbyyear


def subs(string):
    """Perform some string substitutions."""
    string = string.replace("CO2", "CO\ :sub:`2`")
    string = string.replace("1st", "1\ :sup:`st`")
    string = string.replace("2nd", "2\ :sup:`nd`")
    string = string.replace("3rd", "3\ :sup:`rd`")
    string = re.sub(r"(\d+)th", r"\1\ :sup:`th`", string)
    string = gimli.sub('`pyGIMLi\ <http://www.pygimli.org/>`_', string)
    return string


def write_entry(entry, fhandle):
    """ Write beginning on entry. """

    if " and " in entry["author"]:
        authors = entry["author"].split(" and ")
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
            fhandle.write("**%s, %s**" % (name[0], "F\. M\."))
        else:
            fhandle.write("%s, %s" % (name[0], name[1][0] + "\."))
        if i < len(authors) - 1:
            fhandle.write(", ")
        else:
            fhandle.write(" (" + entry["year"] + "): ")

    fhandle.write(subs(entry["title"]) + ". ")


articles = parse_bib("content/articles.bib")
conference = parse_bib("content/conference.bib")

link = "  :raw-html:`<a target=\"_blank\" href=\"/javascript/pdfjs/web/viewer.html?file=%s#pagemode=thumbs\"><i class=\"icon-%s\" title=\"Download PDF\" style=\"color:green\"></i></a>`"
link_ex = "  :raw-html:`<a target=\"_blank\" href=\"%s\"><i class=\"icon-%s\" style=\"color:green\" title=\"Download PDF\"></i></a>`"
#citations = " :raw-html:`<object height=\"50\" data=\"http://api.elsevier.com/content/abstract/citation-count?doi=%s&httpAccept=text/html&apiKey=557b7437b48874840f9cb4d8b0650079\"></object>`"

# Write main file
f = open("content/pages/publications.rst", "w")

f.write("""
Publications
============
:slug: publications

.. role:: raw-html(raw)
   :format: html

Journal articles
----------------
""")

num_articles = 0
for year in articles:
    f.write(year[0] + "\n")
    f.write("^^^^\n\n")

    for article in year[1]:
        try:
            write_entry(article, f)
        except:
            print(article)
            raise
        f.write("*" + article["journal"] + "*")
        if "volume" in article:
            f.write(", ")
            f.write(article["volume"] + ", ")
            f.write(article["pages"])
        else:
            print("No volume info found for", article)

        if "doi" in article:
            if len(article["doi"]) > 3:
                f.write(", ")
                f.write("`DOI:" + article["doi"] + " <https://doi.org/" + article["doi"] + ">`_")

        if "note" in article:
            f.write(" (%s)" % article["note"])

        f.write(". ")

        if "link" in article and len(article["link"]) > 10:
            if article["link"].lower().endswith(".pdf"):
                icon = "file-pdf-o"
            else:
                icon = "external-link"
            if not article["link"].startswith("."):
                f.write(link_ex % (article["link"], icon))
            else:
                f.write(link % (article["link"][1:], icon))
        #if len(article["doi"]) > 3:
        #f.write(citations % article["doi"])
        f.write("\n\n")
        num_articles += 1

f.write("Conference contributions\n")
f.write("------------------------\n\n")

num_conference = 0
for year in conference:
    f.write(year[0] + "\n")
    f.write("^^^^\n\n")

    for article in year[1]:
        try:
            write_entry(article, f)
        except:
            print(article)
            raise
        if 'booktitle' in article:
            f.write(subs(article["booktitle"]))
        elif 'series' in article:
            f.write(subs(article["series"]))
        else:
            f.write("*Conference Proceeding*")
        if 'doi' in article:
            f.write(", `DOI:" + article["doi"] + " <https://doi.org/" +
                    article["doi"] + ">`_")

        if "note" in article:
            f.write(" (%s)" % article["note"])

        f.write(".")
        if "link" in article and len(article["link"]) > 10:
            if article["link"].lower().endswith(".pdf"):
                icon = "file-pdf-o"
            else:
                icon = "external-link"
            if not article["link"].startswith("."):
                f.write(link_ex % (article["link"], icon))
            else:
                f.write(link % (article["link"][1:], icon))
        f.write("\n\n")
        num_conference += 1

print(
    "Wrote %d journals articles and %d conference contributions to publications.rst."
    % (num_articles, num_conference))

f.write("""
.. class:: sidenote

  :icon:`file-pdf-o` A PDF version of my CV including this list of publications can be downloaded `here </static/cv_fwagner.pdf>`_.
""")
f.close()
