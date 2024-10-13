from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.place.models import Place as mPlace
from src.marker.models import Marker as mMarker
from src.user.types import UserTypeID


async def get_places(
    db: AsyncSession, user_id: UserTypeID, skip: int = 0, limit: int = 100
):
    result = await db.execute(
        select(mPlace).filter(mPlace.id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()


async def get_markers(
    db: AsyncSession, user_id: UserTypeID, skip: int = 0, limit: int = 100
):
    result = await db.execute(
        select(mMarker).filter(mMarker.id == user_id).offset(skip).limit(limit)
    )
    return result.scalars().all()
