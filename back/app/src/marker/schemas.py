from pydantic import BaseModel


class PlaceIdMarkerIdPatch(BaseModel):
    place_id: int


class MarkerBase(BaseModel):
    address: str
    lat: float
    lng: float
    category: str


class MarkerCreate(MarkerBase):
    pass


class Marker(MarkerBase):
    id: int
    created_at: int

    class Config:
        from_attributes = True
