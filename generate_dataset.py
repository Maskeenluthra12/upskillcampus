import os
import numpy as np
import pandas as pd

np.random.seed(42)

rows = 15000

dates = pd.date_range(
    start="2024-01-01",
    periods=rows,
    freq="h"
)

weather_types = ["Clear", "Cloudy", "Rain", "Fog"]

data = []

for date in dates:

    hour = date.hour
    month = date.month
    weekday = date.weekday()

    temperature = np.random.randint(15, 41)

    weather = np.random.choice(
        weather_types,
        p=[0.45, 0.30, 0.20, 0.05]
    )

    holiday = np.random.choice(
        ["Yes", "No"],
        p=[0.05, 0.95]
    )

    traffic = 1000

    # Morning Rush
    if 7 <= hour <= 10:
        traffic += 1700

    # Evening Rush
    if 17 <= hour <= 20:
        traffic += 2200

    # Weekends
    if weekday >= 5:
        traffic -= 400

    # Rain
    if weather == "Rain":
        traffic += 500

    # Fog
    if weather == "Fog":
        traffic += 350

    # Holidays
    if holiday == "Yes":
        traffic -= 700

    # Summer
    if month in [5, 6]:
        traffic += 150

    # Temperature Effect
    if temperature > 35:
        traffic += 150

    traffic += np.random.randint(-250, 251)

    traffic = max(250, traffic)

    data.append([
        date,
        temperature,
        weather,
        holiday,
        traffic
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Date",
        "Temperature",
        "Weather",
        "Holiday",
        "Traffic_Volume"
    ]
)

os.makedirs("dataset", exist_ok=True)

df.to_csv(
    "dataset/traffic_dataset.csv",
    index=False
)

print("="*50)
print("Dataset Generated Successfully!")
print("="*50)
print(df.head())
print("\nShape:", df.shape)