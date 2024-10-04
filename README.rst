..  Copyright (c) 2024, Janus Heide.
..  All rights reserved.
..
.. Distributed under the "BSD 3-Clause License", see LICENSE.rst.

Brundle
=======

.. image:: https://github.com/janusheide/brundle/actions/workflows/unittests.yml/badge.svg
    :target: https://github.com/janusheide/brundle/actions/workflows/unittests.yml
    :alt: Unit tests

.. image:: https://img.shields.io/pypi/pyversions/brundle
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/librariesio/github/janusheide/brundle
   :alt: Libraries.io dependency status for GitHub repo


Runs various linters if they are installed.

Getting Started
---------------

Install and run::

    pip install brundle
    brundle --help

    usage: brundle [-h] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--log-file LOG_FILE] [-v]

    Run available linters.

    options:
    -h, --help            show this help message and exit
    --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                            Logging level. (default: WARNING)
    --log-file LOG_FILE   Pipe loggining to file instead of stdout. (default: None)
    -v, --version         show program's version number and exit


Or if you want to install all linters that brundle bundles::

    pip install brundle[linters]


Usage
-----

Run::

    brundle

Runs all the following programs in order, and return 1 if any of them result in an error.

    1. licensecheck
    2. isort
    3. ruff
    4. mypy


Development
-----------

Setup, run tests and release::

    pip install .[dev]
    brundle
    pytest
    bouillon release 1.2.3
