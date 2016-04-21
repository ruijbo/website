#!/bin/bash

tex="pdflatex -interaction=nonstopmode cv.tex"

pandoc ../pages/publications.rst -o publications.tex

sed -i '1,2d' publications.tex
sed -i '/quote/d' publications.tex
sed -i 's/\\sub/\\/g' publications.tex
sed -i 's/\\subsection/\\textbf/g' publications.tex

# Delete raw html (newer pandoc versions do it automatically)
sed -i 's/:raw-html:/\n\n:raw-html:/g' publications.tex
sed -i '/:raw-html:/,/^$/d' publications.tex
sed -i 's/^$/\\vspace{0.22cm}\n/g' publications.tex

# Make CO2 subscript
sed -i 's/CO2/CO\\textsubscript{2}/g' publications.tex
sed -i 's/1st/1\\textsuperscript{st}/g' publications.tex
sed -i 's/2nd/2\\textsuperscript{nd}/g' publications.tex
sed -i 's/3rd/3\\textsuperscript{rd}/g' publications.tex

($tex && $tex && $tex) || echo "PDF compilation failed."
if [[ -f cv.pdf ]]; then
    echo "Moving new PDF to download folder."
    mv -f cv.pdf ../static/cv_fwagner.pdf
fi
