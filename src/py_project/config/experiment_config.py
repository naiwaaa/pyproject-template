from __future__ import annotations

from typing import Generic, Literal, TypeVar

from pydantic import PositiveInt, DirectoryPath, PositiveFloat
from pydantic.generics import GenericModel

from py_project.config.base_config import BaseConfig


class BaseModelConfig(BaseConfig):
    pass


ModelConfigT = TypeVar("ModelConfigT", bound="BaseModelConfig")


class DataConfig(BaseConfig):
    data_dir: DirectoryPath


class TrainingConfig(BaseConfig):
    loss_func: Literal["mse"]
    optimizer: Literal["adam"]

    max_epochs: PositiveInt
    batch_size: PositiveInt
    learning_rate: PositiveFloat


class WandbConfig(BaseConfig):
    project: str
    tags: list[str]
    resume: bool


class MiscConfig(BaseConfig):
    seed: PositiveInt | None


class ExperimentConfig(BaseConfig, GenericModel, Generic[ModelConfigT]):
    data: DataConfig
    model: ModelConfigT
    training: TrainingConfig
    wandb: WandbConfig
    misc: MiscConfig | None
