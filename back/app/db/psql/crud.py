from sqlalchemy.orm import Session

from . import models, schemas


def get_place(db: Session, place_id: int):
    return db.query(models.Marker).filter(models.Marker.id == place_id).first()


def get_markers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Marker).offset(skip).limit(limit).all()
