import time
from sensors import TemperatureSensor, CPUSensor
from monitor import SensorMonitor


sensors = [
    TemperatureSensor("Living Room", threshold=28.0),
    TemperatureSensor("Garage", threshold=40.0),
    CPUSensor("My PC")
]

monitor = SensorMonitor(sensors, interval=3)

try:
    monitor.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    monitor.stop()
