from datetime import datetime


class AlertSystem:
    def __init__(self):
        self.alert_log = []

    def check(self, status):
        if status["warning"]:
            alert = {
                "sensor": status["name"],
                "value": status["value"],
                "unit": status["unit"],
                "threshold": status["threshold"],
                "time": status["time"]
            }
            self.alert_log.append(alert)
            self._print_alert(alert)

    def _print_alert(self, alert):
        print(f"ALERT! {alert['sensor']} reached {alert['value']}{alert['unit']} "
              f"(limit: {alert['threshold']}{alert['unit']}) at {alert['time']}")

    def get_alerts(self):
        return self.alert_log

    def summary(self):
        if not self.alert_log:
            print("No alerts triggered.")
            return
        print(f"\n--- Alert Summary ({len(self.alert_log)} total) ---")
        for a in self.alert_log:
            print(f"  {a['time']} | {a['sensor']}: {a['value']}{a['unit']}")
