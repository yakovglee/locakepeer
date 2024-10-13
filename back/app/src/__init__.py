__all__ = ["Marker", "Place", "User"]


from .marker.models import *
from .place.models import *
from .user.models import *

from fastapi import APIRouter
from .marker.api import router as marker_router
from .place.api import router as place_router

from src.user.users import fastapi_users
from src.user.auth import auth_backend
from src.user.schemas import UserCreate, UserRead

routers = APIRouter()

routers.include_router(
    marker_router,
    prefix="/markers",
    tags=["Markers"],
)

routers.include_router(
    place_router,
    prefix="/places",
    tags=["Places"],
)

routers.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

routers.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)
