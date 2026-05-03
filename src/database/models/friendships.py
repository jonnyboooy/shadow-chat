import enum
from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class FriendshipStatus(enum.Enum):
    """Статусы дружеских связей"""
    PENDING = "pending"       # Запрос отправлен, ожидает подтверждения
    ACCEPTED = "accepted"     # Дружба подтверждена
    BLOCKED = "blocked"       # Один из пользователей заблокировал другого


class Friendship(BaseModel):
    """
    Модель дружеских связей между пользователями.
    
    Позволяет создавать список друзей и управлять статусом взаимодействия.
    """
    __tablename__ = "friendships"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор связи"
    )
    user1_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID первого пользователя"
    )
    user2_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID второго пользователя"
    )
    status: Mapped[FriendshipStatus] = mapped_column(
        default=FriendshipStatus.PENDING,
        comment="Статус дружеской связи"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания связи"
    )
    accepted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время подтверждения дружбы"
    )
