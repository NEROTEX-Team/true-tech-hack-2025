from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    route_class=DishkaRoute,
)
