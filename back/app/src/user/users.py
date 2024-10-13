from .manager import get_user_manager
from .auth import auth_backend
from .types import UserTypeID

from fastapi_users import FastAPIUsers

from .db import User

fastapi_users = FastAPIUsers[User, UserTypeID](
    get_user_manager,
    [auth_backend],
)
