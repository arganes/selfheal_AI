from fastapi import APIRouter
from app.services.self_healing_service import run_self_healing

router = APIRouter()

@router.post("/self-heal")
def self_heal():
    return run_self_healing()