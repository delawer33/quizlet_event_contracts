from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class LearningEventType(StrEnum):
    LEARNING_SESSION_STARTED = "learning_session_started"
    LEARNING_SESSION_FINISHED = "learning_session_finished"


class LearningSessionStarted(BaseModel):
    session_id: int
    user_id: int
    deck_id: int
    started_at: datetime


class LearningSessionFinished(BaseModel):
    session_id: int
    user_id: int
    deck_id: int
    finished_at: datetime
    total_cards_seen: int
    learned_cards: int
    duration_sec: int
    completed: bool
