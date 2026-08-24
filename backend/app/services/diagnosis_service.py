def diagnose_system(cpu_usage: float, memory_usage: float):
    issues = []

    if cpu_usage >= 80:
        issues.append("High CPU usage")

    if memory_usage >= 80:
        issues.append("High memory usage")

    if issues:
        return {
            "status": "issue_detected",
            "issues": issues
        }

    return {
        "status": "healthy",
        "issues": []
    }