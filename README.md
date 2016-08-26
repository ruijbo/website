Source code for personal website www.fwagner.info
=================================================

[![Build Status](https://travis-ci.org/florian-wagner/website.svg)](https://travis-ci.org/florian-wagner/website)

Built with [Pure Theme](http://purepelican.com/) for
[Pelican](http://blog.getpelican.com/). Uses icons by
[FontAwesome](http://fontawesome.io/) and
[Academicons](http://jpswalsh.github.io/academicons/).

To build and serve website locally:

``` bash
sudo pip install pelican bibtexparser
git clone --recursive https://github.com/florian-wagner/website.git
cd website
make html
make serve
# open http://localhost:8000 in your browser
```
