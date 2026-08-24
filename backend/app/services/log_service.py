from datetime import datetime

def create_log(event: str, message: str):
    return {
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "message": message
    }