from fastapi import FastAPI

from .config import settings
from .api.healthcheck.endpoints import router as healthcheck_router
from .api.v0.router import api_v0_router


app = FastAPI(
    root_path=settings.ROOT_PATH,
    title=settings.SERVICE_NAME,
    contact={"name": "jonnyboooy", "email": "akvartanyan@mail.ru"},
    description="Shadow Chat's API Gateway",
    version="0.0.1",
)

app.include_router(healthcheck_router)
app.include_router(api_v0_router)
