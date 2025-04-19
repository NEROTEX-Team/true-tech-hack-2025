from dataclasses import dataclass, field
from os import environ


@dataclass(frozen=True, slots=True, kw_only=True)
class MWSConfig:
    secret_key: str = field(default_factory=lambda: environ["APP_MWS_SECRET_KEY"])
    url: str = field(default_factory=lambda: environ["APP_MWS_URL"])
