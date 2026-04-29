from fastapi import APIRouter, status

from .schema import HealthCheckResponseSchema


router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"]
)


@router.get(
    "/",
    description="Application health check"
)
async def app_health_check() -> HealthCheckResponseSchema:
    return HealthCheckResponseSchema(
        status="OK",
    )
