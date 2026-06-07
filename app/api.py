from fastapi import APIRouter, HTTPException, status
from .models import Reminder, ReminderCreate
from .service import service


router = APIRouter()


@router.post("/", response_model=Reminder)  # default 200, not 201 → spec mismatch
async def create_reminder(reminder: ReminderCreate):
    """
    Create a new reminder.

    NOTE: For this demo, the endpoint currently returns 200 OK by default.
    The API spec says it should return 201 Created, which the PR review agent
    is expected to catch.
    """
    try:
        created = service.create_reminder(reminder)
    except ValueError as exc:
        # Basic 400 mapping for invalid payloads
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc

    return created


@router.get("/{reminder_id}", response_model=Reminder)
async def get_reminder(reminder_id: int):
    """
    Retrieve a single reminder by its ID.
    """
    reminder = service.get_reminder(reminder_id)
    if reminder is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reminder not found.",
        )
    return reminder


@router.get("/")
async def list_reminders() -> list:
    """
    Temporary stub endpoint.

    Later PRs will introduce proper models, persistence, and additional routes:
    - POST /reminders
    - GET /reminders/{id}
    """
    return []
