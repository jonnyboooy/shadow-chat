from datetime import datetime, date

from sqlalchemy import func, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class Profile(BaseModel):
    """
    Модель профиля пользователя.
    
    Хранит расширенную информацию о пользователе: личные данные, контактные данные.
    Связана с User через profile_id для аутентификации.
    """
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор профиля"
    )
    first_name: Mapped[str] = mapped_column(
        comment="Имя пользователя"
    )
    last_name: Mapped[str | None] = mapped_column(
        comment="Фамилия пользователя (опционально)"
    )
    patronymic: Mapped[str | None] = mapped_column(
        comment="Отчество пользователя (опционально)"
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date,
        comment="Дата рождения пользователя"
    )
    avatar_url: Mapped[str] = mapped_column(
        comment="Ссылка на аватар пользователя"
    )
    phone_number: Mapped[str | None] = mapped_column(
        unique=True,
        comment="Номер телефона пользователя (опционально)"
    )
    email: Mapped[str | None] = mapped_column(
        unique=True,
        comment="Почтовый адрес пользователя (опционально)"
    )
    bio: Mapped[str | None] = mapped_column(
        comment="Краткое описание пользователя"
    )
    location: Mapped[str | None] = mapped_column(
        comment="Местоположение пользователя"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата создания профиля"
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        comment="Дата последнего обновления профиля"
    )
