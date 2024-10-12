from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import Integer, Sequence, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


from db.psql.db import Base

if TYPE_CHECKING:
    from src.place.models import Place


class Marker(Base):

    __tablename__ = "marker"

    id: Mapped[int] = mapped_column(
        Sequence("marker_id_seq", start=1000, increment=1),
        primary_key=True,
    )
    address: Mapped[str]
    lat: Mapped[float]
    lng: Mapped[float]
    category: Mapped[str]
    created_at: Mapped[int] = mapped_column(
        Integer, default=func.extract("epoch", func.now())
    )

    place: Mapped[Optional[List["Place"]]] = relationship(back_populates="marker")
