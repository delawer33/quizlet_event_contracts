from datetime import datetime

from pydantic import BaseModel


class DeckCreated(BaseModel):
    deck_id: int
    author_id: int
    created_at: datetime


class CardCreated(BaseModel):
    card_id: int
    deck_id: int
    created_at: datetime
