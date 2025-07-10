import random
import time
import json

def generate_sensor_data():
    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(25, 80), 2),
        "vibration": round(random.uniform(0.1, 1.5), 2)
    }

def is_anomaly(data):
    return data["temperature"] > 70 or data["vibration"] > 1.2

# Example usage
data = generate_sensor_data()
data["anomaly"] = is_anomaly(data)
print(json.dumps(data, indent=2))