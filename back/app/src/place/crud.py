from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()


def get_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Place).offset(skip).limit(limit).all()


def create_place(db: Session, item: schemas.PlaceCreate):
    db_item = models.Place(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def upd_markerid(db: Session, place_id: int, marker_id: int):
    db.query(models.Place).filter(models.Place.id == place_id).update(
        {"marker_id": marker_id}
    )
    db.commit()
    return db.query(models.Place).filter(models.Place.id == place_id).one_or_none()
