import random
import psutil
from datetime import datetime


class Sensor:
    def __init__(self, name, unit, threshold):
        self.name = name
        self.unit = unit
        self.threshold = threshold
        self._last_value = None
        self._last_read_time = None

    def read(self):
        raise NotImplementedError("Subclass must implement read()")

    def get_status(self):
        value = self.read()
        self._last_value = value
        self._last_read_time = datetime.now()

        return {
            "name": self.name,
            "value": value,
            "unit": self.unit,
            "threshold": self.threshold,
            "warning": value > self.threshold,
            "time": self._last_read_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, threshold={self.threshold})"


class TemperatureSensor(Sensor):
    def __init__(self, name="Temperature Sensor", threshold=30.0):
        super().__init__(name, "°C", threshold)

    def read(self):
        # simulating sensor data for now
        return round(random.uniform(18.0, 45.0), 1)


class CPUSensor(Sensor):
    def __init__(self, name="CPU Sensor", threshold=85.0):
        super().__init__(name, "%", threshold)

    def read(self):
        return psutil.cpu_percent(interval=1)
