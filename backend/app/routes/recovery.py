from fastapi import APIRouter
from app.services.recovery_service import recover_system

router = APIRouter()

@router.post("/recovery")
def start_recovery():
    return recover_system()