from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class UserBlock(BaseModel):
    """
    Модель блокировки пользователей.
    
    Хранит информацию о том, какие пользователи заблокировали других пользователей.
    Позволяет создавать черный список и предотвращать взаимодействие.
    """
    __tablename__ = "user_blocks"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор блокировки"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, который выполнил блокировку"
    )
    blocked_user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID заблокированного пользователя"
    )
    blocked_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время блокировки"
    )
    reason: Mapped[str | None] = mapped_column(
        comment="Причина блокировки (опционально)"
    )
