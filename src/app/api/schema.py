from pydantic import BaseModel


class StatusResponseSchema(BaseModel):
    status: str


class DetailResponseSchema(BaseModel):
    detail: str
