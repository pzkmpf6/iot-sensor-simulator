import sqlite3
import threading
from datetime import datetime


class DatabaseLogger:
    def __init__(self, db_path="smart_home.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._lock = threading.Lock()  # додаємо lock
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS sensor_logs (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            name      TEXT,
            value     REAL,
            unit      TEXT,
            threshold REAL,
            warning   INTEGER,
            timestamp TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def log(self, status):
        query = """
        INSERT INTO sensor_logs (name, value, unit, threshold, warning, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        with self._lock:  # тільки один потік пише за раз
            self.conn.execute(query, (
                status["name"],
                status["value"],
                status["unit"],
                status["threshold"],
                int(status["warning"]),
                status["time"]
            ))
            self.conn.commit()

    def get_history(self, limit=10):
        query = """
        SELECT name, value, unit, warning, timestamp
        FROM sensor_logs
        ORDER BY id DESC
        LIMIT ?
        """
        cursor = self.conn.execute(query, (limit,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
