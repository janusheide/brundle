# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

from pathlib import Path

import pytest

from brundle import __version__
from brundle.brundle import cli, main_cli


def test_main_cli():
    assert main_cli() is None


def test_cli():
    with pytest.raises(SystemExit):
        assert cli(["--version"])

    with pytest.raises(SystemExit):
        assert cli(["--help"])

    a = vars(cli(["--log-file", "log.temp", "--log-level", "INFO"]))
    assert a["log_file"] == Path("log.temp")
    assert a["log_level"] == "INFO"


def test_version():
    assert __version__
