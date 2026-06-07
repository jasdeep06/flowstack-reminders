# Testing Guide

Every PR that changes API behavior must include tests that assert the public contract, not the current implementation accident.

For reminder priority changes, tests must cover:

- `POST /reminders/` returns `201 Created` on success.
- Provided priority round-trips through create and get.
- Omitted priority defaults to `normal`.
- Invalid priority values return `422`.
- Past `due_at` still returns `400`.
- Missing reminder lookup still returns `404`.

Tests should avoid comments that bless known spec mismatches. If the implementation currently returns the wrong status code, the test should expose the mismatch instead of encoding it as expected behavior.
