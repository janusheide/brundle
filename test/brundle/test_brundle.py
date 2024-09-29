import subprocess

from brundle import __version__, run_linters


def test_brundle():
    run_linters()


def test_cli():
    subprocess.run("brundle")


def test_version():
    assert __version__
