from typing import Dict, Optional

from .models import ReminderCreate, Reminder


class ReminderRepository:
    """
    Very simple in-memory repository for demo purposes.
    (In a real service, this would be backed by a database.)
    """

    def __init__(self) -> None:
        self._data: Dict[int, Reminder] = {}
        self._next_id: int = 1

    def create(self, payload: ReminderCreate):
        reminder = Reminder(
            id=self._next_id,
            title=payload.title,
            due_at=payload.due_at,
            channel=payload.channel or "email",
            status="scheduled",
        )
        self._data[self._next_id] = reminder
        self._next_id += 1
        return reminder

    def get(self, reminder_id: int) -> Optional[Reminder]:
        return self._data.get(reminder_id)
