from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


from db.psql.db import Base

if TYPE_CHECKING:
    from src.place.models import Place


class Marker(Base):

    __tablename__ = "marker"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    address: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
    category: Mapped[str]
    created_at: Mapped[int] = mapped_column(
        Integer, default=func.extract("epoch", func.now())
    )

    place_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("place.id"), nullable=True
    )
    place: Mapped[list["Place"]] = relationship(back_populates="marker")
