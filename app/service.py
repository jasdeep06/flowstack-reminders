from datetime import datetime, timezone

from .models import ReminderCreate, Reminder
from .notifications import NotificationClient
from .repository import ReminderRepository


class ReminderService:
    """
    Application service for reminders.

    Handles validation and coordinates repository and notifications.
    """

    def __init__(
        self, repository: ReminderRepository, notifications: NotificationClient
    ) -> None:
        self.repository = repository
        self.notifications = notifications

    def create_reminder(self, payload: ReminderCreate):
        # Basic business validation: due_at must be in the future (UTC-based check).
        if payload.due_at <= datetime.now(timezone.utc):
            raise ValueError("due_at must be in the future")

        reminder = self.repository.create(payload)

        # Intentionally using print instead of logger for the demo.
        print("Created reminder", reminder.id)

        self.notifications.send_preview(reminder)
        return reminder

    def get_reminder(self, reminder_id: int) -> Reminder | None:
        return self.repository.get(reminder_id)


# Simple singleton-style wiring for this demo
repository = ReminderRepository()
notifications = NotificationClient()
service = ReminderService(repository, notifications)
