from fastapi import APIRouter
from app.services.healing_service import start_healing

router = APIRouter()

@router.post("/heal")
def heal_system():
    return start_healing()