__all__ = ["Marker", "Place", "User"]


from .marker.models import *
from .place.models import *
from .user.models import *

from fastapi import APIRouter
from .marker.api import router as marker_router
from .place.api import router as place_router


routers = APIRouter()

routers.include_router(marker_router, prefix="/markers", tags=["Маркеры"])
routers.include_router(place_router, prefix="/places", tags=["Места"])
