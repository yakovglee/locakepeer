from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.config import settings

DATABASE_URL = f"postgresql+asyncpg://{settings.PSQL.POSTGRES_USER}:{settings.PSQL.POSTGRES_PASSWORD}@{settings.PSQL.POSTGRES_HOST}:{settings.PSQL.POSTGRES_PORT}/{settings.PSQL.POSTGRES_DB}"

engine = create_async_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
async def get_db():
    db = AsyncSession()
    try:
        yield db
    finally:
        await db.close()
