import enum
from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class ReportType(enum.Enum):
    """Типы жалоб"""
    SPAM = "spam"               # Спам
    HARMFUL = "harmful"         # Вредоносный контент
    HARASSMENT = "harassment"   # Преследование
    INSULT = "insult"           # Оскорбление
    COPYRIGHT = "copyright"     # Нарушение авторских прав
    OTHER = "other"             # Другое


class ReportStatus(enum.Enum):
    """Статусы жалоб"""
    PENDING = "pending"         # Рассматривается
    IN_PROGRESS = "in_progress" # В обработке
    RESOLVED = "resolved"       # Решена
    REJECTED = "rejected"       # Отклонена


class Report(BaseModel):
    """
    Модель жалоб на пользователей или сообщения.
    
    Позволяет пользователям сообщать о нарушениях,
    а администраторам управлять рассмотрением жалоб.
    """
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор жалобы"
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, который подал жалобу"
    )
    report_type: Mapped[ReportType] = mapped_column(
        comment="Тип жалобы"
    )
    reported_user_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, на которого подана жалоба"
    )
    reported_message_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="CASCADE"
        ),
        comment="ID сообщения, на которое подана жалоба"
    )
    description: Mapped[str | None] = mapped_column(
        comment="Описание нарушения"
    )
    status: Mapped[ReportStatus] = mapped_column(
        default=ReportStatus.PENDING,
        comment="Текущий статус жалобы"
    )
    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        comment="Дата и время завершения рассмотрения"
    )
    resolved_by_id: Mapped[int | None] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="SET NULL"
        ),
        comment="ID администратора, который рассмотрел жалобу"
    )
    admin_comment: Mapped[str | None] = mapped_column(
        comment="Комментарий администратора"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время подачи жалобы"
    )
