from fastapi import APIRouter
from app.services.log_service import create_log

router = APIRouter()

@router.get("/logs")
def get_logs():
    return create_log(
        event="system_check",
        message="Self Healing AI is running normally"
    )