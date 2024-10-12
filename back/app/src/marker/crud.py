from sqlalchemy.orm import Session

from . import models
from . import schemas

from src.place.models import Place


def get_marker(db: Session, marker_id: int):
    return db.query(models.Marker).filter(models.Marker.id == marker_id).first()


def get_markers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Marker).offset(skip).limit(limit).all()


def create_marker(db: Session, item: schemas.MarkerCreate):
    db_item = models.Marker(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def upd_place_markerid(db: Session, place_id: int, marker_id: int):
    db.query(Place).filter(Place.id == place_id).update({"marker_id": marker_id})
    db.commit()
    return db.query(Place).filter(Place.id == place_id).one_or_none()
