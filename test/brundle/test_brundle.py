# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

from brundle import __version__
from brundle.brundle import cli, main_cli


def test_main_cli():
    assert main_cli() is None


def test_cli():
    assert cli(["--help"])
    assert cli(["--version"])

    a = vars(cli(["--log_file", "log.temp", "--log_level", "INFO"]))
    a["log_file"] == "log.temp"
    a["log_level"] == "INFO"


def test_version():
    assert __version__
