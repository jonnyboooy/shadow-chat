import enum
from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class Role(enum.Enum):
    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class ChatMember(BaseModel):
    __tablename__ = "chat_members"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="ID"
    )
    chat_id: Mapped[int] = mapped_column(
        ForeignKey(
            "chats.id",
            ondelete="CASCADE"
        ),
        comment="ID чата"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя"
    )
    joined_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата вступления в чат"
    )
    role: Mapped[str] = mapped_column(
        default=Role.MEMBER,
        comment="Роль в чате (owner/admin/member)"
    )
