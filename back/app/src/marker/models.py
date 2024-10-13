from typing import TYPE_CHECKING, List, Optional

from sqlalchemy import ForeignKey, Integer, Sequence, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship


from db.psql.db import Base
from src.user.types import UserTypeID

if TYPE_CHECKING:
    from src.place.models import Place
    from src.user.models import User


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

    user_id: Mapped[UserTypeID] = mapped_column(
        ForeignKey("user.id", ondelete="cascade"), nullable=False
    )

    place: Mapped[Optional[List["Place"]]] = relationship(back_populates="marker")
    user: Mapped["User"] = relationship(back_populates="marker")
