# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

from __future__ import annotations

import asyncio
from argparse import (
    ArgumentDefaultsHelpFormatter, ArgumentParser, FileType, Namespace,
)
from importlib.metadata import version
from logging import basicConfig, getLevelName, getLogger
from pathlib import Path
from subprocess import CalledProcessError, run

from packaging.requirements import Requirement

try:
    from tomllib import load  # type: ignore
except ModuleNotFoundError:
    from tomli import load  # type: ignore


logger = getLogger(__name__)


def run_linters(dependencies: list[str]) -> None:

    run_failed = False

    if "licensecheck" in dependencies:
        logger.info("Running licensecheck")
        try:
            run(["licensecheck", "--zero"], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if "isort" in dependencies:
        logger.info("Running isort")
        try:
            run(["isort", "."], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if "ruff" in dependencies:
        logger.info("Running ruff check")
        try:
            run(["ruff", "check"], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if "mypy" in dependencies:
        logger.info("Running mypy")
        try:
            run(["mypy", "."], shell=False, check=True)
        except CalledProcessError:
            run_failed = True


    if run_failed:
        exit(1)


def parse_arguments() -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser(
        description="Update Python Project Dependencies.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-i",
        "--infile",
        nargs="*",
        default="pyproject.toml",
        type=FileType("rb"),
        help="Path to input file",
    )

    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level.",
    )

    parser.add_argument(
        "--log-file", type=Path, help="Pipe loggining to file instead of stdout."
    )

    parser.add_argument("-v", "--version", action="version", version=version("flies"))

    return parser.parse_args()


async def main(*, infile: FileType, log_file: Path, log_level: str) -> None:
    """Main."""
    basicConfig(
        filename=log_file,
        level=getLevelName(log_level),
        format="%(levelname)s: %(message)s",
    )

    data = load(infile) #type: ignore
    project = data.get("project")
    if project is None:
        logger.critical(f"No project section in input file: {infile}")
        exit(1)

    if optional_dep := project.get("optional-dependencies"):
        run_linters(
            [Requirement(d).name for deps in optional_dep.values() for d in deps])

    else:
        logger.exception(f"Could not find 'optional-dependencies' in: {infile}")
        exit(1)


def main_cli() -> None:
    """Main."""
    args = parse_arguments()
    asyncio.run(main(**vars(args)))


if __name__ == "__main__":
    main_cli()
