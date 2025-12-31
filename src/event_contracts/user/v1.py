from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class UserEventType(StrEnum):
    USER_REGISTERED = "user_registered"


class UserRegistered(BaseModel):
    user_id: int
    email: str
    registered_at: datetime
