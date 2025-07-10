# 🛠️ Smart Sensor Dashboard for Predictive Maintenance

A real-time web dashboard that simulates industrial sensor data (temperature and vibration), detects anomalies, and visualizes trends using Python, Flask, and Chart.js.

## 🎯 Project Objective

This project demonstrates how predictive maintenance systems can be built using simulated sensor data. It mimics real-world industrial setups where sensors monitor equipment health, and anomalies are flagged before failures occur.

## 🚀 Features

- 📡 Real-time sensor data simulation (temperature & vibration)
- ⚠️ Anomaly detection based on threshold logic
- 📊 Dynamic charts using Chart.js
- 🧠 API endpoints for live data and historical logs
- 💾 Stores last 100 readings in a local JSON file
- 🖥️ Simple, responsive web interface

## 🧱 Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Backend     | Python + Flask    |
| Frontend    | HTML + CSS + JS   |
| Charts      | Chart.js          |
| Data Store  | JSON (local file) |

## 📂 Folder Structure
smart-sensor-dashboard/ 
    ├── app.py                  # Flask app 
    ├── sensor_simulator.py     # Sensor data generator 
    ├── templates/ 
    │   └── index.html          # Frontend UI 
    ├── static/ │   
    └── style.css           # Styling 
    ├── data/ │   
    └── history.json        # Sensor history (last 100 readings)
