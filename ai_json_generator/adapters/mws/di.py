from collections.abc import AsyncIterator

from aiohttp import ClientSession
from dishka import BaseScope, Component, Provider, Scope, provide

from ai_json_generator.adapters.mws.client import MWSClient
from ai_json_generator.adapters.mws.config import MWSConfig
from ai_json_generator.domain.interfaces.mws.client import IMWSClient


class MWSProvider(Provider):
    def __init__(
        self,
        config: MWSConfig,
        scope: BaseScope | None = None,
        component: Component | None = None,
    ):
        super().__init__(scope, component)
        self._config = config

    @provide(scope=Scope.APP)
    async def session(self) -> AsyncIterator[ClientSession]:
        async with ClientSession() as session:
            yield session

    @provide(scope=Scope.APP)
    async def mws_client(self, session: ClientSession) -> IMWSClient:
        return MWSClient(
            secret_key=self._config.secret_key,
            url=self._config.url,
            session=session,
            client_name="mws",
        )
