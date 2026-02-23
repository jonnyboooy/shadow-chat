from sqlalchemy.ext.asyncio import AsyncSession

from ..core import connection
from ..models import User


class UsersRepository:
    @staticmethod
    @connection
    async def get_user_by_id(user_id: int, session: AsyncSession):
        return await session.get(User, user_id)
