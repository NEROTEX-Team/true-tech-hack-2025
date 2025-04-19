from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from ai_json_generator.adapters.mws.di import MWSProvider
from ai_json_generator.presentors.rest.config import Config
from ai_json_generator.shared.logging import setup_logging


def get_application() -> FastAPI:
    config = Config()
    return build_app(config=config)


def build_app(config: Config) -> FastAPI:
    setup_logging(log_level=config.logging.log_level, use_json=config.logging.use_json)
    container = make_async_container(MWSProvider(config=config.mws))

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        yield

        await container.close()

    app = FastAPI(
        title=config.app.title,
        description=config.app.description,
        version=config.app.version,
        lifespan=lifespan,
    )

    setup_dishka(container=container, app=app)

    return app
