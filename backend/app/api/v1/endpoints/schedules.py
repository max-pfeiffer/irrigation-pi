from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def create_schedule() -> int:
    """
    Create Schedule
    """
    pass
