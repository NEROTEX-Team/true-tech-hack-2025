from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

router = APIRouter(
    prefix="/models",
    tags=["models"],
    route_class=DishkaRoute,
)
