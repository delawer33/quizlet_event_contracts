from datetime import datetime

from pydantic import BaseModel


class CourseCreated(BaseModel):
    course_id: int
    author_id: int
    created_at: datetime


class CourseEnrolled(BaseModel):
    course_id: int
    user_id: int
    enrolled_at: datetime


class CourseProgressUpdated(BaseModel):
    course_id: int
    user_id: int
    deck_id: int
    progress_percent: float
    updated_at: datetime
