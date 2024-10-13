from src.user.users import fastapi_users
from src.user.auth import auth_backend
from src.user.schemas import UserCreate, UserRead, UserUpdate

from fastapi import APIRouter

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

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    tags=["User"],
)
