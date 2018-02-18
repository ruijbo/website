#!/bin/bash

tex="pdflatex -interaction=nonstopmode cv.tex"
pubtex="publications.tex"

pandoc ../pages/publications.rst -o tmp.tex

head -n -3 tmp.tex > $pubtex
sed -i '/journal-articles/,$!d' $pubtex
sed -i '/quote/d' $pubtex
sed -i 's/\\sub/\\/g' $pubtex
sed -i 's/\\subsection/\\textbf/g' $pubtex

# Delete raw html (newer pandoc versions do it automatically)
sed -i 's/:raw-html:/\n\n:raw-html:/g' $pubtex
sed -i '/:raw-html:/,/^$/d' $pubtex
sed -i 's/^$/\\vspace{0.22cm}\n/g' $pubtex

# Make CO2 subscript
sed -i 's/CO2/CO$_2$/g' $pubtex
sed -i 's/1st/1\\textsuperscript{st}/g' $pubtex
sed -i 's/2nd/2\\textsuperscript{nd}/g' $pubtex
sed -i 's/3rd/3\\textsuperscript{rd}/g' $pubtex

($tex && $tex && $tex) || echo "PDF compilation failed."
if [[ -f cv.pdf ]]; then
    echo "Moving new PDF to download folder."
    mv -f cv.pdf ../static/cv_fwagner.pdf
fi
