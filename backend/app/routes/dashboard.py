from fastapi import APIRouter
from app.services.dashboard_service import get_dashboard_summary

router = APIRouter()


@router.get("/dashboard")
def dashboard():
    return get_dashboard_summary()