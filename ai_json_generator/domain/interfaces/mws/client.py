from collections.abc import Sequence
from typing import Protocol

from ai_json_generator.domain.entities.mws.model import MWSModel


class IMWSClient(Protocol):
    async def fetch_models(self) -> Sequence[MWSModel]: ...
