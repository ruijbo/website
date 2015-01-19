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

from collections import defaultdict

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

    if "CO2" in entry["title"]:
        title = entry["title"].replace("CO2", "CO\ :sub:`2`\ ")
    else:
        title = entry["title"]

    fhandle.write(title + ". ")

articles = parse_bib("content/articles.bib")
conference = parse_bib("content/conference.bib")

f = open("./content/pages/publications.rst", "w")

f.write("Publications\n")
f.write("============\n\n")

f.write("Journal articles\n")
f.write("----------------\n\n")

for year in articles:
    f.write(year[0] + "\n")
    f.write("^^^^\n\n")

    for article in year[1]:
        write_entry(article, f)
        f.write("*" + article["journal"] + "*, ")
        f.write(article["volume"] + ", ")
        f.write(article["pages"] + ", ")
        f.write("http://dx.doi.org/" + article["doi"] + ".\n\n")


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

f.close()
