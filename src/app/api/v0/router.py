from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from .schema import ErrorResponseSchema
from .users.endpoints import router as user_router


api_v0_router = APIRouter(
    prefix="/api/v0",
    default_response_class=ORJSONResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": ErrorResponseSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponseSchema},
    },
)

api_v0_router.include_router(user_router)
