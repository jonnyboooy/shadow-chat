from datetime import datetime, date

from sqlalchemy import func, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class Profile(BaseModel):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="ID"
    )
    first_name: Mapped[str] = mapped_column(
        comment="Имя"
    )
    second_name: Mapped[str] = mapped_column(
        comment="Фамилия"
    )
    patronymic: Mapped[str | None] = mapped_column(
        comment="Отчество"
    )
    date_of_birth: Mapped[date] = mapped_column(
        Date,
        comment="Дата рождения"
    )
    avatar_url: Mapped[str] = mapped_column(
        comment="Ссылка на аватар"
    )
    phone_number: Mapped[str] = mapped_column(
        comment="Номер телефона"
    )
    email: Mapped[str] = mapped_column(
        unique=True,
        comment="Почта"
    )
    hashed_password: Mapped[str] = mapped_column(
        comment="Hash пароля"
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
