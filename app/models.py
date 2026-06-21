from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class ReminderCreate(BaseModel):
    title: str
    due_at: datetime
    channel: Optional[str] = "email"

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("title must be non-empty")
        return value


class Reminder(BaseModel):
    id: int
    title: str
    due_at: datetime
    channel: str
    status: str
