import functools

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from .config import settings


engine = create_async_engine(url=settings.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class BaseModel(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


def connection(method):
    @functools.wraps(method)
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                result = await method(*args, session=session, **kwargs)

                if session.new or session.dirty or session.deleted:
                    await session.commit()

                return result
            except Exception as e:
                await session.rollback()
                raise
            finally:
                await session.close()

    return wrapper
