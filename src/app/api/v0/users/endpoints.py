from fastapi import APIRouter, status, Response
from fastapi import status

from .schema import UserResponseSchema, DetailResponseSchema
from .service import UsersService


router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": DetailResponseSchema,
        },
    },
)


@router.get(
    "/{user_id}",
    description="Application health check",
    responses={
        status.HTTP_200_OK: {
            "model": UserResponseSchema,
        },
    },
)
async def get_user_by_id(
    user_id: int,
    response: Response,
) -> UserResponseSchema | DetailResponseSchema:
    try:
        return await UsersService.get_by_id(user_id)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return DetailResponseSchema(detail=str(e))
