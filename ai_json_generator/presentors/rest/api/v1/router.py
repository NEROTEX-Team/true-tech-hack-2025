from fastapi import APIRouter

from ai_json_generator.presentors.rest.api.v1.chat.router import router as chat_router
from ai_json_generator.presentors.rest.api.v1.models.router import (
    router as models_router,
)

router = APIRouter(prefix="/v1")
router.include_router(chat_router)
router.include_router(models_router)
