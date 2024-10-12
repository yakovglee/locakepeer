import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src.marker import models, schemas
from core.config import settings
from src.marker import crud
from db.psql.db import SessionLocal


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/places/", response_model=list[schemas.Marker])
def get_markers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_markers(db, skip=skip, limit=limit)
    return places


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.FASTApi.host, port=settings.FASTApi.port, reload=True
    )
