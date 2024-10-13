from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.psql.db import get_db

from . import schemas, crud
from src.place.crud import upd_markerid as mPlace_upd_markerid

from src.place.schemas import Place as sPlace
from src.user.models import User
from src.user.users import current_active_user

router = APIRouter()


@router.post("/", response_model=schemas.Marker)
async def create_markers(
    item: schemas.MarkerCreate,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_active_user),
):
    created_item = await crud.create_marker(db=db, item=item, user_id=user.id)
    return created_item


@router.get("/{marker_id}", response_model=schemas.Marker)
async def read_marker(marker_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_marker(db=db, marker_id=marker_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Marker not found")
    return db_item


@router.patch("/{marker_id}", response_model=sPlace)
async def upd_markerid_in_place(
    place_id: schemas.PlaceIdMarkerIdPatch,
    marker_id: int,
    db: AsyncSession = Depends(get_db),
):
    db_item = await mPlace_upd_markerid(
        db=db, place_id=place_id.place_id, marker_id=marker_id
    )
    if db_item is None:
        raise HTTPException(status_code=404, detail="Change is unavailable")
    return db_item


@router.get("/", response_model=list[schemas.Marker])
async def read_markers(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    items = await crud.get_markers(db=db, skip=skip, limit=limit)
    return items
