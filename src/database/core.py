from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from .config import settings


engine = create_async_engine(url=settings.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
