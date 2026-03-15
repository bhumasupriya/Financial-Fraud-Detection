import streamlit as st
import pandas as pd
import requests
import numpy as np
import time
import plotly.express as px

st.title("💳 Real-Time Fraud Detection Dashboard")

fraud_count = 0
safe_count = 0

chart_data = pd.DataFrame({"Fraud": [0], "Safe": [0]})
chart = st.line_chart(chart_data)

for i in range(200):
    transaction = np.random.rand(30).tolist()
    res = requests.post(
        "http://127.0.0.1:5000/predict",
        json={"data": transaction}
    ).json()

    if res["fraud"] == 1:
        fraud_count += 1
    else:
        safe_count += 1

    new_data = pd.DataFrame({
        "Fraud": [fraud_count],
        "Safe": [safe_count]
    })

    chart.add_rows(new_data)
    time.sleep(1)
