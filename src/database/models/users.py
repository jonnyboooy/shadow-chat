from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="ID"
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey(
            "profiles.id",
            ondelete="CASCADE"
        ),
    )
    status: Mapped[str | None] = mapped_column(
        comment="Статус пользователя"
    )
    last_seen: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата последнего посещения"
    )
    is_online: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Статус онлайн"
    )
