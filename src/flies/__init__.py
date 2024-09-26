
# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

"""Import flies functions."""

from importlib.metadata import PackageNotFoundError, version

from flies.flies import run_linters

try:
    __version__ = version("flies")
except PackageNotFoundError:
    pass

__all__ = (
    "run_linters",
)
