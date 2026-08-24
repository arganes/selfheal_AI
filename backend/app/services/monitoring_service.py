import psutil


def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    return {
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage,
        "service": "running"
    }