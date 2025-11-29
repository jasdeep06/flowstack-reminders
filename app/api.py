from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_reminders() -> list:
    """
    Temporary stub endpoint.

    Later PRs will introduce proper models, persistence, and additional routes:
    - POST /reminders
    - GET /reminders/{id}
    """
    return []
