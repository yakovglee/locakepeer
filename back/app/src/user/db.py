from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase


from .models import User
from db.psql.db import get_db


async def get_user_db(session=Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)
