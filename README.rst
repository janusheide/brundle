..  Copyright (c) 2024, Janus Heide.
..  All rights reserved.
..
.. Distributed under the "BSD 3-Clause License", see LICENSE.rst.

Update Python Project Dependencies (UPPD)
=========================================

.. image:: https://github.com/janusheide/flies/actions/workflows/unittests.yml/badge.svg
    :target: https://github.com/janusheide/flies/actions/workflows/unittests.yml
    :alt: Unit tests

.. image:: https://img.shields.io/pypi/pyversions/flies
   :alt: PyPI - Python Version

.. image:: https://img.shields.io/librariesio/github/janusheide/flies
   :alt: Libraries.io dependency status for GitHub repo


Runs various linters if they are present in the optional dependencies in pyproject.toml file.

Getting Started
---------------

Install and run::

    pip install flies
    flies --help

Usage
-----

Run::
    flies

Runs all the following programs in order, and return 1 if any of them gives and error.
    1. licensecheck
    2. isort
    3. ruff
    4. mypy


Development
-----------

Setup, run tests and release::

    pip install .[dev]
    flies
    pytest
    python boil.py release
