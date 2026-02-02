from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class Message(BaseModel):
    __tablename__ = "messages"

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
    sender_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID отправителя"
    )
    content: Mapped[str] = mapped_column(
        comment="Текст сообщения"
    )
    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата отправки"
    )
    is_read: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Прочитано ли сообщение"
    )
