from collections.abc import Sequence
from http import HTTPStatus
from types import MappingProxyType

from aiohttp import ClientSession
from asyncly import BaseHttpClient, ResponseHandlersType
from asyncly.client.handlers.pydantic import parse_model
from pydantic import BaseModel
from yarl import URL

from ai_json_generator.domain.entities.mws.model import MWSModel
from ai_json_generator.domain.interfaces.mws.client import IMWSClient


class MWSModelSchema(BaseModel):
    id: str
    object: str
    owned_by: str


class MWSModelSchemaResponse(BaseModel):
    data: Sequence[MWSModelSchema]


class MWSClient(BaseHttpClient, IMWSClient):
    FETCH_MODEL_HANDLERS: ResponseHandlersType = MappingProxyType(
        {
            HTTPStatus.OK: parse_model(MWSModelSchemaResponse),
        }
    )

    def __init__(
        self,
        secret_key: str,
        url: URL | str,
        session: ClientSession,
        client_name: str,
    ):
        super().__init__(url, session, client_name)
        self._auth_header = {
            "Authorization": f"Bearer {secret_key}",
        }

    async def fetch_models(self) -> list[MWSModel]:
        response = await self._make_req(
            method="GET",
            url=self._url / "v1/models",
            headers=self._auth_header,
            handlers=self.FETCH_MODEL_HANDLERS,
        )
        return [
            MWSModel(
                id=model.id,
                object=model.object,
                owned_by=model.owned_by,
            )
            for model in response.data
        ]
