from sensors import TemperatureSensor, CPUSensor
from monitor import SensorMonitor
from dashboard import run_dashboard


sensors = [
    TemperatureSensor("Living Room", threshold=28.0),
    TemperatureSensor("Garage", threshold=40.0),
    CPUSensor("My PC")
]

monitor = SensorMonitor(sensors, interval=3)

run_dashboard(monitor)
