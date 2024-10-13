from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from . import models
from . import schemas


async def get_place(db: AsyncSession, place_id: int):
    result = await db.execute(select(models.Place).filter(models.Place.id == place_id))
    return result.scalar_one_or_none()


async def get_places(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(models.Place).offset(skip).limit(limit))
    return result.scalars().all()


async def create_place(db: AsyncSession, item: schemas.PlaceCreate, user_id: int):
    db_item = models.Place(**item.model_dump())
    db_item.user_id = user_id
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def upd_markerid(db: AsyncSession, place_id: int, marker_id: int):

    stmt = (
        update(models.Place)
        .where(models.Place.id == place_id)
        .values(marker_id=marker_id)
    )
    await db.execute(stmt)
    await db.commit()

    result = await db.execute(select(models.Place).filter(models.Place.id == place_id))
    return result.scalar_one_or_none()
