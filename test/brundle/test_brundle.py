from pathlib import Path

try:
    from tomllib import load  # type: ignore
except ModuleNotFoundError:
    from tomli import load  # type: ignore

import subprocess

from brundle import __version__, optional_dependencies, run_linters


def test_get_dependencies():
    with Path("pyproject.toml").open("rb") as pf:
        project = load(pf).get("project")
        assert "mypy" in optional_dependencies(project.get("optional-dependencies"))


def test_brundle():
    run_linters([])


def test_cli():
    subprocess.run("brundle")


def test_version():
    assert __version__
