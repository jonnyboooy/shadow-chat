from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse

from .schema import DetailResponseSchema
from .users.endpoints import router as user_router


api_v0_router = APIRouter(
    prefix="/api/v0",
    default_response_class=ORJSONResponse,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": DetailResponseSchema},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": DetailResponseSchema},
    },
)

api_v0_router.include_router(user_router)
