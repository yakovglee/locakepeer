from fastapi_users import schemas

from .types import UserTypeID


class UserRead(schemas.BaseUser[UserTypeID]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass
