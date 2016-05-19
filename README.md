# PyTemplate
![Build Status][travis]

Everything you need to start building a new Python package.

Based off of the Python project structuring guidelines in the wonderful 
[Hitchhiker's Guide to Python][hhgp] by @kennethreiz, but tailored to my
preferences and use-cases.

Code should follow [PEP 8][pep8] (Python coding style) and 
[PEP 257][pep257] (Docstring Conventions) whenever possible.

Sphinx is more documentation overhead than I want to get into right now so we're 
using Markdown and [MkDocs][mkdocs] to serve .md as nice html pages. mkdocs.yml 
configures how the page is built.

Continuous integration using [Travis][travis] is configured using .travis.yml. 
Unit tests are run with [nose][nose] and are contained in the /tests folder.

You can choose to run everything in a [Docker][docker] container (including documentation hosting on port 8000) by configuring the Dockerfile.

[travis]: https://travis-ci.org/Shaun1/PyTemplate.svg?branch=master
[hhgp]: http://docs.python-guide.org/en/latest/writing/structure/
[pep8]: https://www.python.org/dev/peps/pep-0008/
[pep257]: https://www.python.org/dev/peps/pep-0257/
[nose]: http://nose.readthedocs.io/en/latest/
[mkdocs]: http://www.mkdocs.org/
[travis]: https://travis-ci.org/
[docker]: http://www.docker.com/
