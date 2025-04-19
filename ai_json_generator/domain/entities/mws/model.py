from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class MWSModel:
    id: str
    object: str
    owned_by: str
