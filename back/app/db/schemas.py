from pydantic import BaseModel


class InfoSpot(BaseModel):
    id: int
    name_en: str
    name_ko: str
    description: str | None
    lat: float
    lng: float
    insta: str | None
    namuWiki: str | None
    ctgr: str