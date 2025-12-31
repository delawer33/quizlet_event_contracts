from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel


class ContentEventType(StrEnum):
    DECK_CREATED = "deck_created"
    CARD_CREATED = "card_created"


class DeckCreated(BaseModel):
    deck_id: int
    author_id: int
    created_at: datetime


class CardCreated(BaseModel):
    card_id: int
    deck_id: int
    created_at: datetime
