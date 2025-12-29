from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EventEnvelope(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)
    event_type: str
    # Learning:
    #   learning_session_started
    #   learning_session_finished
    # Courses:
    #   course_created
    #   course_enrolled
    #   course_progress_updated
    # Content:
    #   deck_created
    #   card_created
    # Users:
    #   user_registered

    event_version: int = 1
    occured_at: datetime
    producer: str
    payload: dict

    def to_json(self):
        return self.model_dump_json()
