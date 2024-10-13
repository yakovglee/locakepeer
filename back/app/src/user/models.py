from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, Sequence
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from sqlalchemy.ext.declarative import declared_attr
from db.psql.db import Base
from sqlalchemy.orm import relationship
from .types import UserTypeID

if TYPE_CHECKING:
    from src.marker.models import Marker
    from src.place.models import Place


class User(SQLAlchemyBaseUserTable[UserTypeID], Base):
    id: Mapped[UserTypeID] = mapped_column(
        Integer,
        Sequence("user_id_seq", start=-259484, increment=5),
        primary_key=True,
    )

    marker: Mapped[list["Marker"] | None] = relationship(back_populates="user")
    place: Mapped[list["Place"] | None] = relationship(back_populates="user")


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
        )
