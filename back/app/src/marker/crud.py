from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models
from . import schemas

from src.place.models import Place
from src.place.crud import upd_markerid


async def get_marker(db: AsyncSession, marker_id: int):
    result = await db.execute(
        select(models.Marker).filter(models.Marker.id == marker_id)
    )
    return result.scalar_one_or_none()


async def get_markers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Marker).offset(skip).limit(limit))
    return result.scalars().all()


async def create_marker(db: AsyncSession, item: schemas.MarkerCreate, user_id: int):
    db_item = models.Marker(**item.model_dump())
    db_item.user_id = user_id
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
