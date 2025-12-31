from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class CourseEventType(StrEnum):
    COURSE_CREATED = "course_created"
    COURSE_ENROLLED = "course_enrolled"
    COURSE_PROGRESS_UPDATED = "course_progress_updated"


class CourseCreated(BaseModel):
    course_id: int
    author_id: int
    created_at: datetime


class CourseEnrolled(BaseModel):
    enrollment_id: int
    course_id: int
    user_id: int
    enrolled_at: datetime


class CourseProgressUpdated(BaseModel):
    course_id: int
    user_id: int
    deck_id: int
    progress_percent: float
    updated_at: datetime
