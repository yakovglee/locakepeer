import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from core.config import settings
from db.psql import crud, models, schemas
from db.psql.db import SessionLocal


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/places/", response_model=list[schemas.Places])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host=settings.FASTApi.host, port=settings.FASTApi.port, reload=True
    )
