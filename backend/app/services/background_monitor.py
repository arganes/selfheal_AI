import threading
import time

from app.services.auto_monitor_service import run_monitoring_cycle


def start_background_monitor(interval: int = 30):
    def monitor():
        while True:
            try:
                run_monitoring_cycle()
            except Exception as error:
                print(f"Background monitoring error: {error}")

            time.sleep(interval)

    thread = threading.Thread(target=monitor, daemon=True)
    thread.start()