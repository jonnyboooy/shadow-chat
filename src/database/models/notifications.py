import enum
from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class NotificationType(enum.Enum):
    """Типы уведомлений"""
    NEW_MESSAGE = "new_message"           # Новое сообщение
    NEW_FRIEND_REQUEST = "new_friend_request"  # Новый запрос в друзья
    FRIEND_REQUEST_ACCEPTED = "friend_request_accepted"  # Запрос принят
    MESSAGE_READ = "message_read"         # Сообщение прочитано
    SYSTEM = "system"                     # Системное уведомление
    ADMIN_MESSAGE = "admin_message"       # Сообщение от администратора


class Notification(BaseModel):
    """
    Модель уведомлений.
    
    Позволяет отправлять и управлять уведомлениями пользователям
    о событиях в чатах, друзьях и системных событиях.
    """
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор уведомления"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, которому отправлено уведомление"
    )
    notification_type: Mapped[NotificationType] = mapped_column(
        comment="Тип уведомления"
    )
    title: Mapped[str] = mapped_column(
        comment="Заголовок уведомления"
    )
    message: Mapped[str] = mapped_column(
        comment="Текст уведомления"
    )
    related_id: Mapped[int | None] = mapped_column(
        comment="ID связанного объекта (сообщение, чат, пользователь)"
    )
    is_read: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Прочитано ли уведомление"
    )
    read_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время прочтения уведомления"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания уведомления"
    )
