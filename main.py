from monitor import SensorMonitor
from sensors import TemperatureSensor, CPUSensor
import time
cat > main.py << 'EOF'


sensors = [
    TemperatureSensor("Living Room", threshold=28.0),
    TemperatureSensor("Garage", threshold=40.0),
    CPUSensor("My PC")
]

monitor = SensorMonitor(sensors, interval=3)

try:
    monitor.start()
    # keep main thread alive while background threads work
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    monitor.stop()
EOF
