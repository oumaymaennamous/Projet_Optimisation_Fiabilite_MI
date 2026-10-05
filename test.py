import requests

data = {
    "torque": 200.0,
    "tool_wear": 200.0,
    "rotational_speed": 1500.0,
    "air_temperature": 600.0,
    "process_temperature": 350.0,
    "type": "H"
}

try:
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")