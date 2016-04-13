#!/bin/bash

pandoc ../pages/publications.rst -o publications.tex
sed -i '1,7d' publications.tex
sed -i '/quote/d' publications.tex
sed -i 's/\\sub/\\/g' publications.tex
sed -i 's/\\subsection/\\textbf/g' publications.tex
sed -i 's/^$/\\vspace{0.25cm}\n/g' publications.tex
texfot pdflatex cv.tex && mv -f cv.pdf ../static/cv_fwagner.pdf

