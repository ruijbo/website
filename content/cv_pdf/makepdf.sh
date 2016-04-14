#!/bin/bash

tex="pdflatex -interaction=nonstopemode cv.tex"

pandoc ../pages/publications.rst -o publications.tex
sed -i '1,2d' publications.tex
sed -i '/quote/d' publications.tex
sed -i 's/\\sub/\\/g' publications.tex
sed -i 's/\\subsection/\\textbf/g' publications.tex
sed -i 's/^$/\\vspace{0.22cm}\n/g' publications.tex
sed -i 's/:raw-html:.*$//g' publications.tex
($tex && $tex && $tex) || echo "PDF compilation failed."
if [[ -f cv.pdf ]]; then
    echo "Moving new PDF to download folder."
    mv -f cv.pdf ../static/cv_fwagner.pdf
fi
