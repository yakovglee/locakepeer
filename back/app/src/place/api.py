from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.psql.db import get_db

from . import schemas, crud

router = APIRouter()


@router.post("/", response_model=schemas.Place)
def create_places(item: schemas.PlaceCreate, db: Session = Depends(get_db)):
    return crud.create_place(db=db, item=item)


@router.get("/{place_id}", response_model=schemas.Place)
def read_item(place_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_place(db=db, place_id=place_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Place not found")
    return db_item


@router.put("/{place_id}", response_model=schemas.Place)
def read_item(place_id: int, marker_id: int, db: Session = Depends(get_db)):
    db_item = crud.upd_markerid(db=db, place_id=place_id, marker_id=marker_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Change is unavailable")
    return db_item


@router.get("/", response_model=list[schemas.Place])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_places(db=db, skip=skip, limit=limit)
    return items
