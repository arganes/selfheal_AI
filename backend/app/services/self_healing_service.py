from datetime import datetime

from app.services.monitoring_service import get_system_status
from app.services.diagnosis_service import diagnose_system
from app.services.recovery_service import recover_system
from app.services.history_service import add_history


def run_self_healing():
    system_status = get_system_status()

    diagnosis = diagnose_system(
        system_status["cpu_usage_percent"],
        system_status["memory_usage_percent"]
    )

    if diagnosis["status"] == "issue_detected":
        recovery = recover_system()
    else:
        recovery = {
            "recovery": "not_required",
            "status": "system_healthy"
        }

    result = {
        "timestamp": datetime.now().isoformat(),
        "monitoring": system_status,
        "diagnosis": diagnosis,
        "recovery": recovery
    }

    add_history(result)

    return result