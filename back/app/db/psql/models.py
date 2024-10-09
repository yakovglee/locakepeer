from datetime import datetime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from .db import Base


class Places(Base):

    __tablename__ = "places"

    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
    category: Mapped[str]
    created_at: Mapped[datetime]
