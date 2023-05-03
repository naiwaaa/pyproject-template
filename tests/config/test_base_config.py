from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from py_project.config import BaseConfig


if TYPE_CHECKING:
    from pathlib import Path


class MinimalConfig(BaseConfig):
    number: int


@pytest.mark.parametrize(
    "minimal_config_file_fixture",
    ["minimal_yaml_config_file", "minimal_toml_config_file", "minimal_json_config_file"],
)
def test_read_config_from_file_should_success(
    request: pytest.FixtureRequest,
    minimal_config_file_fixture: str,
) -> None:
    config_file: Path = request.getfixturevalue(minimal_config_file_fixture)

    result = MinimalConfig.read_from_file(config_file)

    assert result.number == 10


def test_read_config_from_file_should_fail_with_unsupported_file_format(
    tmp_path: Path,
) -> None:
    config_file = tmp_path / "random.random"
    config_file.write_text("")

    with pytest.raises(AssertionError, match="`.random` is not supported"):
        MinimalConfig.read_from_file(config_file)
