from dataclasses import dataclass, field
from os import environ

from ai_json_generator.adapters.mws.config import MWSConfig
from ai_json_generator.shared.logging import LoggingConfig


@dataclass(frozen=True, slots=True, kw_only=True)
class AppConfig:
    title: str = field(
        default_factory=lambda: environ.get("APP_TITLE", "AI JSON Generator")
    )
    version: str = field(default_factory=lambda: environ.get("APP_VERSION", "1.0.0"))
    description: str = field(default_factory=lambda: environ.get("APP_DESCRIPTION", ""))
    debug: bool = field(
        default_factory=lambda: environ.get("DEBUG", "false").lower() == "true"
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    app: AppConfig = field(default_factory=AppConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    mws: MWSConfig = field(default_factory=MWSConfig)
