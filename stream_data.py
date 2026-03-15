import requests
import numpy as np
import time

API_URL = "http://127.0.0.1:5000/predict"

while True:
    # Generate random transaction
    transaction = np.random.rand(30).tolist()

    response = requests.post(API_URL, json={"data": transaction})
    result = response.json()

    if result["fraud"] == 1:
        print("🚨 FRAUD DETECTED")
    else:
        print("✅ Safe transaction")

    time.sleep(1)
