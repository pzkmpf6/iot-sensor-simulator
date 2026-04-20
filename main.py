from sensors import Sensor, TemperatureSensor, CPUSensor


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

print("=== Smart Home Monitor ===\n")

# test that base class cant be used directly
try:
    s = Sensor("test", "x", 0)
    s.read()
except NotImplementedError as e:
    print(f"base class blocked: {e}\n")

for sensor in sensors:
    print_status(sensor.get_status())
