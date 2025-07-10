from flask import Flask, jsonify, render_template
from sensor_simulator import generate_sensor_data, is_anomaly
import json
import os

app = Flask(__name__)

HISTORY_FILE = "data/history.json"

# Ensure history file exists
if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "w") as f:
        json.dump([], f)

def save_to_history(data):
    try:
        with open(HISTORY_FILE, "r+") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []

            history.append(data)
            if len(history) > 100:
                history = history[-100:]
            f.seek(0)
            json.dump(history, f, indent=2)
            f.truncate()
    except Exception as e:
        print("Error saving to history:", e)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sensor")
def sensor():
    data = generate_sensor_data()
    data["anomaly"] = is_anomaly(data)
    save_to_history(data)
    return jsonify(data)

@app.route("/history")
def history():
    with open(HISTORY_FILE, "r") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(debug=True)