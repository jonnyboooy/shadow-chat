from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class User(BaseModel):
    """
    Модель пользователя системы.
    
    Хранит аутентификационные данные и основную информацию о пользователе.
    Связана с Profile для хранения расширенной информации.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор пользователя"
    )
    profile_id: Mapped[int] = mapped_column(
        ForeignKey(
            "profiles.id",
            ondelete="CASCADE"
        ),
        unique=True,
        comment="Ссылка на профиль пользователя"
    )
    username: Mapped[str | None] = mapped_column(
        unique=True,
        comment="Уникальное имя пользователя для входа"
    )
    email: Mapped[str | None] = mapped_column(
        unique=True,
        comment="Почтовый адрес пользователя"
    )
    phone_number: Mapped[str | None] = mapped_column(
        unique=True,
        comment="Номер телефона пользователя"
    )
    hashed_password: Mapped[str] = mapped_column(
        comment="Хэш пароля пользователя (не хранится в открытом виде)"
    )
    status: Mapped[str | None] = mapped_column(
        default="online",
        comment="Статус пользователя (online, offline, busy, away)"
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Активен ли аккаунт пользователя"
    )
    is_email_verified: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Подтвержден ли email пользователя"
    )
    last_seen: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время последнего посещения"
    )
    is_online: Mapped[bool] = mapped_column(
        default=False,
        server_default="false",
        comment="Текущий статус онлайн"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата регистрации пользователя"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        comment="Дата последнего обновления данных"
    )
