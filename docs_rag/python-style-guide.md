# Python Service Style Guide

## Type Hints

Public functions and methods in application, service, and repository layers must declare return types.

Examples:

- `def create(self, payload: ReminderCreate) -> Reminder:`
- `def create_reminder(self, payload: ReminderCreate) -> Reminder:`

## Validation Ownership

Use Pydantic models for request-shape validation and constrained field values. Use service methods for cross-field or business validation such as future timestamps.

## Errors

Do not swallow validation detail. Preserve predictable FastAPI response semantics:

- schema and enum validation: `422`
- business rule validation: `400`
- missing resource: `404`

## Imports

Keep imports grouped as standard library, third-party, then local imports. Avoid unused imports.
