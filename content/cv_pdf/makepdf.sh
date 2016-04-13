#!/bin/bash

pandoc ../pages/publications.rst -o publications.tex
sed -i '1,2d' publications.tex
sed -i '/quote/d' publications.tex
sed -i 's/\\sub/\\/g' publications.tex
sed -i 's/\\subsection/\\textbf/g' publications.tex
sed -i 's/^$/\\vspace{0.22cm}\n/g' publications.tex
pdflatex -interaction=nonstopmode cv.tex
pdflatex -interaction=nonstopmode cv.tex && mv -f cv.pdf ../static/cv_fwagner.pdf

