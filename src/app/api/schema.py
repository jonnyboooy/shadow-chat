from pydantic import BaseModel


class SuccessSchema(BaseModel):
    success: bool


class MessageSchema(BaseModel):
    message: str


class BaseResponseSchema(SuccessSchema, MessageSchema):
    ...


class SuccessResponseSchema(BaseResponseSchema):
    success: bool = True


class ErrorResponseSchema(BaseResponseSchema):
    success: bool = False
