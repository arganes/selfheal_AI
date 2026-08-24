from datetime import datetime

from app.services.diagnosis_service import diagnose_system
from app.services.recovery_service import recover_system
from app.services.history_service import add_history


def run_self_healing():
    diagnosis = diagnose_system()
    recovery = recover_system()

    result = {
        "timestamp": datetime.now().isoformat(),
        "status": "self_healing_completed",
        "diagnosis": diagnosis,
        "recovery": recovery,
        "message": "Self-healing cycle completed successfully"
    }

    add_history(result)

    return result