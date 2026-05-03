import enum
from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class ChatType(enum.Enum):
    PERSONAL = "personal"
    GROUP_CHAT = "group_chat"


class Chat(BaseModel):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="ID чата"
    )
    name: Mapped[str] = mapped_column(
        comment="Название чата"
    )
    description: Mapped[str | None] = mapped_column(
        comment="Описание чата (для групповых чатов)"
    )
    avatar_url: Mapped[str] = mapped_column(
        comment="Ссылка на аватар"
    )
    chat_type: Mapped[ChatType] = mapped_column(
        comment="Тип чата"
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Активен ли чат"
    )
    last_message_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время последнего сообщения"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата создания"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        comment="Дата обновления"
    )
