from fastapi import APIRouter
from app.services.ai_service import analyze_system

router = APIRouter()

@router.get("/ai-analysis")
def get_ai_analysis():
    return analyze_system()