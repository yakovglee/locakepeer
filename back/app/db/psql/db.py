from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.config import settings

DATABASE_URL = f"postgresql://{settings.PSQL.POSTGRES_USER}:{settings.PSQL.POSTGRES_PASSWORD}@{settings.PSQL.POSTGRES_HOST}:{settings.PSQL.POSTGRES_PORT}/{settings.PSQL.POSTGRES_DB}"

engine = create_engine(
    DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print(DATABASE_URL)
