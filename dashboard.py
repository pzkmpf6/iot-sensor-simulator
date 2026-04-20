import os
import time
from database import DatabaseLogger


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("=== Smart Home Monitor ===")
    print()
    print("  1. Live sensor readings")
    print("  2. View history from DB")
    print("  3. View alert log")
    print("  4. Exit")
    print()
    return input("Choose: ").strip()


def live_readings(monitor, duration=10):
    clear()
    print(f"Live readings for {duration}s — Ctrl+C to stop early\n")
    monitor.start()
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        pass
    monitor.stop()
    input("\nPress Enter to return to menu...")


def show_history():
    clear()
    db = DatabaseLogger()
    rows = db.get_history(limit=20)
    db.close()

    print("=== Last 20 Records ===\n")

    if not rows:
        print("No records yet.")
    else:
        for name, value, unit, warning, timestamp in rows:
            flag = "(!)" if warning else "   "
            print(f"{flag} {timestamp} | {name}: {value} {unit}")

    input("\nPress Enter to return to menu...")


def show_alerts(monitor):
    clear()
    print("=== Alert Log ===\n")

    alerts = monitor.alerts.get_alerts()

    if not alerts:
        print("No alerts triggered yet.")
    else:
        for a in alerts:
            print(f"  {a['time']} | {a['sensor']}: {a['value']}{a['unit']} "
                  f"(limit: {a['threshold']}{a['unit']})")
        print(f"\nTotal: {len(alerts)} alert(s)")

    input("\nPress Enter to return to menu...")


def run_dashboard(monitor):
    while True:
        clear()
        choice = show_menu()

        if choice == "1":
            live_readings(monitor, duration=10)
        elif choice == "2":
            show_history()
        elif choice == "3":
            show_alerts(monitor)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
            time.sleep(1)
