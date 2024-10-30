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


Runs all the following programs in order, and return 1 if any of them result in an error.

    1. isort
    2. ruff
    3. mypy


Getting Started
---------------

Install and run::

    pip install brundle
    brundle --help

    usage: brundle [-h]
                   [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                   [--log-file LOG_FILE]
                   [--isort ISORT]
                   [--ruff RUFF]
                   [--mypy MYPY]
                   [-v]

    Run available linters.

    options:
    -h, --help            show this help message and exit
    --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                          logging level (default: INFO)
    --log-file LOG_FILE   pipe loggining to file instead of stdout (default: None)
    --isort ISORT         runs isort (default: False)
    --ruff RUFF           runs ruff (default: False)
    --mypy MYPY           runs mypy (default: False)
    -v, --version         show program's version number and exit


Or if you want to install all linters that brundle bundles::

    pip install brundle[linters]
    brundle --help

    usage: brundle [-h]
                   [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                   [--log-file LOG_FILE]
                   [--isort ISORT]
                   [--ruff RUFF]
                   [--mypy MYPY]
                   [-v]

    Run available linters.

    options:
    -h, --help            show this help message and exit
    --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                          logging level (default: INFO)
    --log-file LOG_FILE   pipe loggining to file instead of stdout (default: None)
    --isort ISORT         runs isort (default: True)
    --ruff RUFF           runs ruff (default: True)
    --mypy MYPY           runs mypy (default: True)
    -v, --version         show program's version number and exit


Usage
-----

Run::

    brundle


Development
-----------

Setup, run tests and release::

    pip install .[dev]
    brundle
    pytest
    bouillon release 1.2.3
