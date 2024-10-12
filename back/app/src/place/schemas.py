from pydantic import BaseModel


class PlaceBase(BaseModel):
    head: str
    subhead: str | None = None
    description: str | None = None
    link_inst: str | None = None
    link_tt: str | None = None


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int
    created_at: int
    updated_at: int
    marker_id: int | None = None

    class Config:
        from_attributes = True
