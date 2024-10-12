from sqlalchemy import Integer, func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


from .db import Base


class Place(Base):

    __tablename__ = "place"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    address: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
    category: Mapped[str]
    created_at: Mapped[int] = mapped_column(
        Integer, default=func.extract("epoch", func.now())
    )
