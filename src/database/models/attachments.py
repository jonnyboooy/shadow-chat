import enum
from datetime import datetime

from sqlalchemy import ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from ..core import BaseModel


class AttachmentType(enum.Enum):
    """Типы вложений"""
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    FILE = "file"


class Attachment(BaseModel):
    """
    Модель вложений к сообщениям.
    
    Хранит информацию о файлах, прикрепленных к сообщениям:
    изображения, видео, аудио, документы и другие файлы.
    """
    __tablename__ = "attachments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="Уникальный идентификатор вложения"
    )
    message_id: Mapped[int] = mapped_column(
        ForeignKey(
            "messages.id",
            ondelete="CASCADE"
        ),
        comment="ID сообщения, к которому прикреплен файл"
    )
    uploaded_by_id: Mapped[int] = mapped_column(
        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),
        comment="ID пользователя, который загрузил файл"
    )
    file_type: Mapped[AttachmentType] = mapped_column(
        comment="Тип файла"
    )
    file_name: Mapped[str] = mapped_column(
        comment="Имя файла"
    )
    file_url: Mapped[str] = mapped_column(
        comment="Ссылка для скачивания файла"
    )
    file_size: Mapped[int] = mapped_column(
        comment="Размер файла в байтах"
    )
    mime_type: Mapped[str | None] = mapped_column(
        comment="MIME-тип файла"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время загрузки"
    )
