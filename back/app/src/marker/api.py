from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.psql.db import get_db

from . import schemas, crud

router = APIRouter()


@router.post("/", response_model=schemas.Marker)
def create_markers(item: schemas.MarkerCreate, db: Session = Depends(get_db)):
    return crud.create_marker(db=db, item=item)


@router.get("/{marker_id}", response_model=schemas.Marker)
def read_item(marker_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_marker(db=db, marker_id=marker_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Marker not found")
    return db_item


@router.get("/", response_model=list[schemas.Marker])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_markers(db=db, skip=skip, limit=limit)
    return items
