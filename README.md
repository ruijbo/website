Source code for personal website www.fwagner.info
=================================================

[![Build Status](https://travis-ci.org/florian-wagner/website.svg)](https://travis-ci.org/florian-wagner/website)

Built with [Pure Theme](http://purepelican.com/) for
[Pelican](http://blog.getpelican.com/).

To build and serve website locally:

``` bash
git clone --recursive https://github.com/florian-wagner/website.git
cd website
sudo pip install pelican bibtexparser pelican-fontawesome
make html
make serve
# open http://localhost:8000 in your browser
```
