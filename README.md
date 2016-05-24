# PyTemplate
[![Build Status](https://travis-ci.org/Shaun1/PyTemplate.svg?branch=master)](https://travis-ci.org/Shaun1/PyTemplate)

Everything you need to start building a new Python package.

Based off of the Python project structuring guidelines in the wonderful 
[Hitchhiker's Guide to Python][hhgp] by @kennethreiz, but tailored to my
preferences and use-cases.

Code should follow [PEP 8][pep8] (Python coding style) and 
[PEP 257][pep257] (Docstring Conventions) whenever possible.

Using Markdown and [MkDocs][mkdocs] instead of RsT and Sphinx because they're simpler. MkDocs will serve .md as nice html pages and can be configured with mkdocs.yml. Run the MkDocs server on port 8000 with:
```
mkdocs serve
```

Continuous integration using [Travis][travis] is configured using .travis.yml. 
Unit tests are run with [nose][nose] and are contained in the /tests folder.

You can choose to run everything in a [Docker][docker] container (including documentation hosting on port 8000) by configuring the Dockerfile.
```
docker build -t my-image .
docker run -it my-image
```

Once you are at the bash prompt of the Docker image you should be able to run the unit tests with:
```
nosetests -v
```

[hhgp]: http://docs.python-guide.org/en/latest/writing/structure/
[pep8]: https://www.python.org/dev/peps/pep-0008/
[pep257]: https://www.python.org/dev/peps/pep-0257/
[nose]: http://nose.readthedocs.io/en/latest/
[mkdocs]: http://www.mkdocs.org/
[travis]: https://travis-ci.org/
[docker]: http://www.docker.com/
