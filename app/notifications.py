from .models import Reminder


class NotificationClient:
    """
    Stub notification client.

    For now, it only simulates sending a preview notification.
    """

    def send_preview(self, reminder: Reminder) -> None:
        # In a real implementation, this might enqueue a message
        # to an email or webhook delivery system.
        # Kept intentionally simple for the demo.
        print(f"Sending preview notification for reminder {reminder.id}")
