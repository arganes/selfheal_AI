from app.services.monitoring_service import get_system_status
from app.services.history_service import get_history


def get_dashboard_summary():
    system_status = get_system_status()
    history = get_history()

    return {
        "system": "Self Healing AI",
        "current_status": system_status,
        "total_events": len(history),
        "recent_events": history[-5:]
    }