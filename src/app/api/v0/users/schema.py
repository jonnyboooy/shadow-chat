from datetime import datetime

from pydantic import BaseModel, ConfigDict

from ..schema import DetailResponseSchema


class UserSchema(BaseModel):
    id: int
    profile_id: int
    status: str | None = None
    last_seen: datetime | None = None
    is_online: bool

    model_config = ConfigDict(from_attributes=True)


class UserResponseSchema(UserSchema):
    result: UserSchema
