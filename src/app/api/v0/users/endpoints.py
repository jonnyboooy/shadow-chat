from fastapi import APIRouter
from fastapi import status

from app.api.healthcheck.schema import ErrorResponseSchema
from app.api.schema import SuccessResponseSchema


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ErrorResponseSchema,
        },
    },
)


@router.get(
    "/{id}",
    description="Application health check",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessResponseSchema,
        },
    },
)
async def app_health_check(
    user_id: int
):
    """
    Получение информации о юзере по ID

    :param user_id: ID юзера
    :return: Pydantic схема с данными о найденном пользователе или None, если таковой не был найден
    """
    ...
