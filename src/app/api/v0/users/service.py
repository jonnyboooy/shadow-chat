import logging

from database.repositories import UsersRepository
from .schema import UserResponseSchema, UserSchema


logger = logging.getLogger(__name__)


class UsersService:
    @classmethod
    async def get_by_id(cls, user_id: int):
        try:
            user = await UsersRepository.get_user_by_id(user_id)
        except Exception:
            logger.exception(f"Ошибка получения пользователя с {user_id=}")
            raise
        else:
            if not user:
                raise Exception

            return UserResponseSchema(
                success=True,
                result=UserSchema.model_validate(user)
            )
