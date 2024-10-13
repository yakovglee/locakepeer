from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)
from fastapi import Depends


from src.user.models import AccessToken
from db.psql.db import get_db


async def get_access_token_db(session=Depends(get_db)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


from src.user.models import AccessToken, User
from core.config import settings


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.AUTH.lifespan)
