# Feature Spec: Reminder Priority

The priority feature lets users mark reminders by operational urgency.

## Accepted Values

Priority is a constrained enum with exactly these lowercase values:

- `low`
- `normal`
- `high`
- `urgent`

The API must reject unknown values such as `soon`, `p0`, `critical`, empty strings, or mixed-case variants unless they are explicitly normalized before validation.

## Defaults

When the client omits `priority`, the service stores `normal` and returns `normal` in every response. The value should not remain `null` after creation.

## Round Trip Behavior

`POST /reminders/` persists priority. `GET /reminders/{id}` returns the stored priority. Future list endpoints should also include priority, but this PR only needs create/get parity.

## Non-Goals For This PR

This PR does not need priority-based sorting, escalation, notification routing, analytics, or UI changes.
