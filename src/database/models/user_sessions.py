from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import JSONB

from ..core import BaseModel


class UserSession(BaseModel):
    """
    Модель активных сессий пользователей.
    
    Позволяет управлять активными сессиями входа, отслеживать устройства
    и обеспечивать безопасность (возможность удаленного выхода).
    """
    __tablename__ = "user_sessions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор сессии"
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя"
    )
    session_token: Mapped[str] = mapped_column(
        comment="Уникальный токен сессии (UUID)"
    )
    device_info: Mapped[dict | None] = mapped_column(
        JSONB,
        comment="Информация об устройстве (UA, OS, браузер)"
    )
    ip_address: Mapped[str | None] = mapped_column(
        comment="IP-адрес пользователя при входе"
    )
    user_agent: Mapped[str | None] = mapped_column(
        comment="User-Agent строки браузера"
    )
    expires_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время истечения сессии"
    )
    is_active: Mapped[bool] = mapped_column(
        default=True,
        server_default="true",
        comment="Активна ли сессия"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания сессии"
    )
    last_activity: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время последней активности"
    )
