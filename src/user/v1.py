from datetime import datetime

from pydantic import BaseModel


class UserRegistered(BaseModel):
    user_id: int
    email: str
    registered_at: datetime
