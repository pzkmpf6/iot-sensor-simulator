# Smart Home IoT Simulator

A Python-based Object-Oriented simulator for monitoring smart home sensors (Temperature, CPU load, etc.). This project demonstrates core concepts of OOP, real-time data monitoring, and database management.

## Features
* **Object-Oriented Design:** Modular `Sensor` base class with specific implementations.
* **Real-time Monitoring:** Simulates sensor data reading using Python multithreading.
* **Data Logging:** Stores sensor history in a local SQLite database.
* **Alert System:** Triggers notifications when thresholds are exceeded (e.g., CPU > 80%).

## Tech Stack
* **Language:** Python 3.12.10
* **Database:** SQLite3
* **Libraries:** `threading`, `sqlite3`, `time`, `psutil` (for PC stats)

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/pzkmpf6/iot-sensor-simulator.git
2. Navigate to the directory:
   ```bash
   cd iot-sensor-simulator
   ```
   
3. Run the simulator:
   ```bash
   python main.py
   ```

## What I Learned (My PWr Journey)
This project was built during my 2nd semester of Informatyczne Systemy Automatyki. It helped me solidify my understanding of:
- Class inheritance and polymorphism in Python.
- Handling concurrent tasks with threading.
- Basic SQL operations using Python.
