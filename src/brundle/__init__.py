
# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

"""Import brundle functions."""

from importlib.metadata import PackageNotFoundError, version

from brundle.brundle import run_linters

try:
    __version__ = version("brundle")
except PackageNotFoundError:
    pass

__all__ = (
    "run_linters",
)
