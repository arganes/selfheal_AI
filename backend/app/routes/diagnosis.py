from fastapi import APIRouter
from app.services.diagnosis_service import diagnose_system

router = APIRouter()

@router.get("/diagnosis")
def get_diagnosis():
    return diagnose_system()