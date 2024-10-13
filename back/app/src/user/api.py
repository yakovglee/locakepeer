from src.user.users import fastapi_users
from src.user.auth import auth_backend
from src.user.schemas import UserCreate, UserRead, UserUpdate
from db.psql.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends
from src.user.models import User
from src.user.users import current_active_user
from src.marker.schemas import Marker as sMarker
from src.place.schemas import Place as sPlace

from . import crud

router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)


user_router = APIRouter()


user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)


@user_router.get("/me/places", response_model=list[sPlace])
async def read_item(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_item = await crud.get_places(db=db, user_id=user.id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Places not found")
    return db_item


@user_router.get("/me/markers", response_model=list[sMarker])
async def read_item(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    db_item = await crud.get_markers(db=db, user_id=user.id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Markers not found")
    return db_item
