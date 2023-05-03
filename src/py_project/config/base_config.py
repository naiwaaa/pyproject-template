from __future__ import annotations

from typing import TypeVar

import json
from pathlib import Path

import yaml
import tomli
from pydantic import BaseSettings


BaseConfigT = TypeVar("BaseConfigT", bound="BaseConfig")


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        allow_mutation = False
        frozen = True

    @classmethod
    def read_from_file(
        cls: type[BaseConfigT],
        config_file: str | Path,
    ) -> BaseConfigT:
        config_file = Path(config_file)
        content = config_file.read_text(encoding="utf-8")

        match (file_format := config_file.suffix):
            case ".json":
                obj = json.loads(content)
            case ".yaml" | ".yml":
                obj = yaml.safe_load(content)
            case ".toml":
                obj = tomli.loads(content)
            case _:
                msg = (
                    f"`{file_format}` is not supported. "
                    "Supported formats: .json, .yaml, .yml, .toml"
                )
                raise AssertionError(msg)

        return cls.parse_obj(obj)
