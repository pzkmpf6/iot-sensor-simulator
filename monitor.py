import threading
import time
from database import DatabaseLogger
from alerts import AlertSystem


class SensorMonitor:
    def __init__(self, sensors, interval=5):
        self.sensors = sensors
        self.interval = interval
        self.db = DatabaseLogger()
        self.alerts = AlertSystem()
        self._running = False
        self._threads = []

    def _poll_sensor(self, sensor):
        while self._running:
            status = sensor.get_status()
            self.db.log(status)
            self.alerts.check(status)

            flag = "(!)" if status["warning"] else "   "
            print(
                f"{flag} [{status['time']}] {status['name']}: {status['value']} {status['unit']}")

            time.sleep(self.interval)

    def start(self):
        self._running = True
        print(
            f"Starting monitor — polling every {self.interval}s. Press Ctrl+C to stop.\n")

        for sensor in self.sensors:
            t = threading.Thread(target=self._poll_sensor, args=(sensor,))
            t.daemon = True
            t.start()
            self._threads.append(t)

    def stop(self):
        self._running = False
        for t in self._threads:
            t.join()
        self.alerts.summary()
        self.db.close()
        print("Monitor stopped.")
