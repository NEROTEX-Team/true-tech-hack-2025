from fastapi import APIRouter

from ai_json_generator.presentors.rest.api.v1.router import router as v1_router

router = APIRouter(prefix="/api")
router.include_router(v1_router)
