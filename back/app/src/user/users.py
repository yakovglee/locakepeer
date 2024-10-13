from .manager import get_user_manager
from .auth import auth_backend
from .types import UserTypeID

from fastapi_users import FastAPIUsers

from .db import User

fastapi_users = FastAPIUsers[User, UserTypeID](
    get_user_manager,
    [auth_backend],
)


current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)
