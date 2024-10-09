from datetime import datetime
from pydantic import BaseModel


class PlacesBase(BaseModel):
    address: str
    lat: str
    lng: str
    category: str


class PlacesCreate(PlacesBase):
    pass


class Places(PlacesBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
