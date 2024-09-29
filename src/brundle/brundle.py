# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

from __future__ import annotations

import asyncio
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from importlib.metadata import version
from importlib.util import find_spec
from logging import basicConfig, getLevelName, getLogger
from pathlib import Path
from subprocess import CalledProcessError, run

logger = getLogger(__name__)


def run_linters() -> None:
    """Run any of the following linters found in the dependencies list,
    and exit with and error if any of them fails.
        1. licensecheck
        2. isort
        3. ruff
        4. mypy
    """
    run_failed = False

    if find_spec("licensecheck"):
        logger.info("Running licensecheck")
        try:
            run(["licensecheck", "--zero"], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if find_spec("isort"):
        logger.info("Running isort")
        try:
            run(["isort", "."], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if find_spec("ruff"):
        logger.info("Running ruff check")
        try:
            run(["ruff", "check"], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if find_spec("mypy"):
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
        description="Run available linters.",
        formatter_class=ArgumentDefaultsHelpFormatter,
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

    parser.add_argument("-v", "--version", action="version", version=version("brundle"))

    return parser.parse_args()


async def main(*, log_file: Path, log_level: str) -> None:
    """Main."""
    basicConfig(
        filename=log_file,
        level=getLevelName(log_level),
        format="%(levelname)s: %(message)s",
    )
    run_linters()


def main_cli() -> None:
    """Main."""
    args = parse_arguments()
    asyncio.run(main(**vars(args)))


if __name__ == "__main__":
    main_cli()
