from typing import TYPE_CHECKING, Optional

from sqlalchemy import ForeignKey, Integer, Sequence, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


from db.psql.db import Base

if TYPE_CHECKING:
    from src.marker.models import Marker


class Place(Base):

    __tablename__ = "place"

    id: Mapped[int] = mapped_column(
        Sequence("place_id_seq", start=1000, increment=1),
        primary_key=True,
        autoincrement=True,
    )
    head: Mapped[str]
    subhead: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    link_inst: Mapped[Optional[str]]
    link_tt: Mapped[Optional[str]]
    created_at: Mapped[int] = mapped_column(
        Integer, default=func.extract("epoch", func.now())
    )
    updated_at: Mapped[int] = mapped_column(
        Integer,
        default=func.extract("epoch", func.now()),
        onupdate=func.extract("epoch", func.now()),
    )

    marker_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("marker.id"), nullable=True
    )

    marker: Mapped[Optional["Marker"]] = relationship(
        back_populates="place",
        foreign_keys=[marker_id],
        remote_side=[marker_id],
    )
