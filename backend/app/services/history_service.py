healing_history = []

def add_history(event: dict):
    healing_history.append(event)
    return event

def get_history():
    return healing_history