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
    or
    pip install brundle[linters] (to install all linters brundle will run.)
    brundle --help

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
    python boil.py release
