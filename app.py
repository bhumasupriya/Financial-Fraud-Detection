from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model + scaler
model = pickle.load(open("fraud_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Home route (to avoid 404)
@app.route("/")
def home():
    return "Fraud Detection API is running"

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]
    data = scaler.transform([data])
    pred = model.predict(data)[0]

    return jsonify({"fraud": int(pred)})

if __name__ == "__main__":
    app.run(port=5000)
