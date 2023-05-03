from __future__ import annotations

from pathlib import Path

import pytest


# ------------------------
# fixtures return file/dir
# ------------------------


def fixtures_dir() -> Path:
    return Path(__file__).parent / "fixtures"


@pytest.fixture()
def minimal_json_config_file() -> Path:
    return fixtures_dir() / "config_files" / "minimal.json"


@pytest.fixture()
def minimal_toml_config_file() -> Path:
    return fixtures_dir() / "config_files" / "minimal.toml"


@pytest.fixture()
def minimal_yaml_config_file() -> Path:
    return fixtures_dir() / "config_files" / "minimal.yaml"
