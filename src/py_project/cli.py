from __future__ import annotations

from pathlib import Path
from argparse import ArgumentParser

import wandb

from py_project import __version__
from py_project.utils import console
from py_project.config import ExperimentConfig
from py_project.config.experiment_config import BaseModelConfig


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    run_experiment(config_file=args.config_file)


def run_experiment(config_file: Path) -> None:
    config = ExperimentConfig[BaseModelConfig].read_from_file(config_file)

    console.print_divider("Init wandb")
    wandb.init(
        project=config.wandb.project,
        resume=config.wandb.resume,
        config=config.dict(),
    )

    console.print_divider("Experiment config")
    console.print_dict(config.dict())

    console.print_divider("Prepare dataset")


def _build_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="py_project", description="Run experiment.")

    parser.add_argument(
        "-c",
        "--config",
        dest="config_file",
        metavar="FILE",
        help="Config file location",
        required=True,
        type=Path,
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print version info",
    )

    return parser
