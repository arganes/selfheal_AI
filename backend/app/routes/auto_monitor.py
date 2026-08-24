from fastapi import APIRouter
from app.services.auto_monitor_service import run_monitoring_cycle

router = APIRouter()


@router.post("/auto-monitor")
def auto_monitor():
    return run_monitoring_cycle()