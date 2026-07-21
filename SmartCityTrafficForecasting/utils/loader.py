import os
import joblib
import pandas as pd


def load_dataset():
    path = "dataset/traffic_dataset.csv"

    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


def load_model():
    path = "model/traffic_model.pkl"

    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found: {path}")

    return joblib.load(path)


def load_encoders():
    weather = "model/weather_encoder.pkl"
    holiday = "model/holiday_encoder.pkl"

    if not os.path.exists(weather):
        raise FileNotFoundError(f"Missing: {weather}")

    if not os.path.exists(holiday):
        raise FileNotFoundError(f"Missing: {holiday}")

    return joblib.load(weather), joblib.load(holiday)