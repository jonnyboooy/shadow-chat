from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class UserSettings(BaseModel):
    """
    Модель настроек пользователя.
    
    Хранит пользовательские настройки приватности, уведомлений
    и других параметров.
    """
    __tablename__ = "user_settings"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор настроек"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        unique=True,
        comment="ID пользователя"
    )
    show_last_seen: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Показывать ли последнее посещение другим пользователям"
    )
    show_phone_number: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Показывать ли номер телефона другим пользователям"
    )
    show_email: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Показывать ли email другим пользователям"
    )
    notify_new_message: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Уведомлять о новых сообщениях"
    )
    notify_new_friend_request: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Уведомлять о новых запросах в друзья"
    )
    notify_message_read: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Уведомлять о прочтении своих сообщений"
    )
    notify_system: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Уведомлять о системных событиях"
    )
    default_chat_theme: Mapped[str | None] = mapped_column(
        comment="Тема чата по умолчанию"
    )
    message_auto_delete: Mapped[int | None] = mapped_column(
        comment="Автоудаление сообщений (в секундах, 0 = выключено)"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания настроек"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        comment="Дата и время обновления настроек"
    )
