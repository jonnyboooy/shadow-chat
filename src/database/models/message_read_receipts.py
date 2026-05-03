from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class MessageReadReceipt(BaseModel):
    """
    Модель подтверждений прочтения сообщений.
    
    Позволяет отслеживать, какие именно пользователи прочитали конкретное сообщение.
    Отличается от is_read в Message тем, что позволяет видеть конкретных прочитавших.
    """
    __tablename__ = "message_read_receipts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор подтверждения"
    )
    message_id: Mapped[int] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="CASCADE"
        ),
        comment="ID сообщения"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, который прочитал сообщение"
    )
    read_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время прочтения"
    )
