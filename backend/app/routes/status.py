from fastapi import APIRouter
from app.services.monitoring_service import get_system_status

router = APIRouter()

@router.get("/status")
def get_status():
    return get_system_status()