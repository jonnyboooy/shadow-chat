from fastapi import APIRouter, status

from .schema import (
    SuccessResponseSchema,
    ErrorResponseSchema
)


router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "model": ErrorResponseSchema,
        },
    }
)


@router.get(
    "/",
    description="Application health check",
    responses={
        status.HTTP_200_OK: {
            "model": SuccessResponseSchema,
        },
    },
)
async def app_health_check():
    return SuccessResponseSchema(
        success=True,
        message="App available!",
    )
