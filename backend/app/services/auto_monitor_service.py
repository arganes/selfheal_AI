import time

from app.services.monitoring_service import get_system_status
from app.services.diagnosis_service import diagnose_system
from app.services.recovery_service import recover_system
from app.services.history_service import add_history


def run_monitoring_cycle():
    system_status = get_system_status()

    diagnosis = diagnose_system(
        system_status["cpu_usage_percent"],
        system_status["memory_usage_percent"]
    )

    recovery = None

    if diagnosis["status"] == "issue_detected":
        recovery = recover_system()

    result = {
        "monitoring": system_status,
        "diagnosis": diagnosis,
        "recovery": recovery
    }

    add_history(result)

    return result