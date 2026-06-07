# Logging And Observability Guide

Application code must use module-level loggers instead of `print`.

Required pattern:

```python
import logging

logger = logging.getLogger(__name__)
```

Use structured context in log messages when helpful, such as `reminder_id`, `channel`, and `priority`. Do not log raw request bodies or user-provided reminder titles because they may contain private information.

Examples:

- Good: `logger.info("created reminder", extra={"reminder_id": reminder.id, "channel": reminder.channel})`
- Bad: `print("Created reminder", reminder.id)`
- Bad: logging the full `ReminderCreate` payload.
