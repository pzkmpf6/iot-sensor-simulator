from sensors import TemperatureSensor, CPUSensor
from database import DatabaseLogger


def print_status(status):
    if status["warning"]:
        label = "WARNING!"
    else:
        label = "OK"

    print(f"[{label}] {status['name']}: {status['value']} {status['unit']} (limit: {status['threshold']})")
    print(f"  time: {status['time']}")
    print()


sensors = [
    TemperatureSensor("Living Room", threshold=28.0),
    TemperatureSensor("Garage", threshold=40.0),
    CPUSensor("My PC")
]

db = DatabaseLogger()

print("=== Smart Home Monitor ===\n")

for sensor in sensors:
    status = sensor.get_status()
    print_status(status)
    db.log(status)

print("--- Last 5 records from DB ---")
for row in db.get_history(limit=5):
    name, value, unit, warning, timestamp = row
    flag = "(!)" if warning else "   "
    print(f"{flag} {timestamp} | {name}: {value} {unit}")

db.close()
