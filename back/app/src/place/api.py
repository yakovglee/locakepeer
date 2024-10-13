from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.psql.db import get_db

from . import schemas, crud

router = APIRouter()


@router.post("/", response_model=schemas.Place)
async def create_places(item: schemas.PlaceCreate, db: AsyncSession = Depends(get_db)):
    created_place = await crud.create_place(db=db, item=item)
    return created_place


@router.get("/{place_id}", response_model=schemas.Place)
async def read_item(place_id: int, db: AsyncSession = Depends(get_db)):
    db_item = await crud.get_place(db=db, place_id=place_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_item


@router.patch("/{place_id}", response_model=schemas.Place)
async def read_item(
    place_id: int,
    marker_id: schemas.MarkerIdPlaceIdPatch,
    db: AsyncSession = Depends(get_db),
):
    db_item = await crud.upd_markerid(
        db=db, place_id=place_id, marker_id=marker_id.marker_id
    )
    if db_item is None:
        raise HTTPException(status_code=404, detail="Change is unavailable")
    return db_item


@router.get("/", response_model=list[schemas.Place])
async def read_items(
    skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)
):
    items = await crud.get_places(db=db, skip=skip, limit=limit)
    return items
