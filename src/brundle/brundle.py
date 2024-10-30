# Copyright (c) 2024, Janus Heide.
# All rights reserved.
#
# Distributed under the "BSD 3-Clause License", see LICENSE.txt.

from __future__ import annotations

import sys
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace
from importlib.metadata import version
from importlib.util import find_spec
from logging import basicConfig, getLevelName, getLogger
from pathlib import Path
from subprocess import CalledProcessError, run

logger = getLogger(__name__)


def run_linters(isort: bool, ruff: bool, mypy: bool, **kwargs) -> None:
    """Run any of the following linters found in the dependencies list,
    and exit with and error if any of them fails.
        1. isort
        2. ruff
        3. mypy
    """
    run_failed = False

    if isort:
        logger.info("Running isort")
        try:
            run(["isort", "."], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if ruff:
        logger.info("Running ruff check")
        try:
            run(["ruff", "check"], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if mypy:
        logger.info("Running mypy")
        try:
            run(["mypy", "."], shell=False, check=True)
        except CalledProcessError:
            run_failed = True

    if run_failed:
        exit(1)


def cli(args) -> Namespace:
    """Parse arguments."""
    parser = ArgumentParser(
        description="Run available linters.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="logging level",
    )
    parser.add_argument(
        "--log-file", type=Path, help="pipe loggining to file instead of stdout"
    )

    parser.add_argument(
        "--isort", type=bool, help="runs isort",
        default=find_spec("isort") is not None
        )
    parser.add_argument(
        "--ruff", type=bool, help="runs ruff",
        default=find_spec("ruff") is not None
        )
    parser.add_argument(
        "--mypy", type=bool, help="runs mypy",
        default=find_spec("mypy") is not None
        )

    parser.add_argument("-v", "--version", action="version", version=version("brundle"))

    return parser.parse_args()


def main(*, log_file: Path, log_level: str, **kwargs) -> None:
    """Main."""
    basicConfig(
        filename=log_file,
        level=getLevelName(log_level),
        format="%(levelname)s: %(message)s",
    )
    run_linters(**kwargs)


def main_cli() -> None:
    """Main."""
    main(**vars(cli(sys.argv[1:])))


if __name__ == "__main__":
    main_cli()
