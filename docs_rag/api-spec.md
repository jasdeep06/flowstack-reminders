# FlowStack Reminders API Specification

## POST /reminders/

Creates a scheduled reminder.

Expected request JSON:

```json
{
  "title": "Submit QBR deck",
  "due_at": "2026-07-01T15:00:00Z",
  "channel": "email",
  "priority": "high"
}
```

Rules:

- `title` is required and must be a non-empty string after trimming whitespace.
- `due_at` is required and must be a future ISO-8601 timestamp.
- `channel` is optional and defaults to `email` when omitted.
- `priority` is optional and must be one of `low`, `normal`, `high`, or `urgent` when provided.
- If `priority` is omitted, the service must store and return `normal`.
- Successful creation must return HTTP `201 Created`.
- Invalid request payloads must return FastAPI/Pydantic validation responses with HTTP `422`.
- Business-rule failures, such as a past `due_at`, must return HTTP `400` with a clear `detail` message.

Expected response JSON includes `id`, `title`, `due_at`, `channel`, `status`, and `priority`.

## GET /reminders/{id}

Returns a reminder by ID.

Rules:

- Existing reminders return HTTP `200 OK`.
- Missing reminders return HTTP `404 Not Found` with `detail: "Reminder not found."`.
- Responses must include the `priority` field.
