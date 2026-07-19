import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Create model folder
os.makedirs("model", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/traffic_dataset.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Feature Engineering
df["Hour"] = df["Date"].dt.hour
df["Day"] = df["Date"].dt.dayofweek
df["Month"] = df["Date"].dt.month

# Encode categorical columns
weather_encoder = LabelEncoder()
holiday_encoder = LabelEncoder()

df["Weather"] = weather_encoder.fit_transform(df["Weather"])
df["Holiday"] = holiday_encoder.fit_transform(df["Holiday"])

# Features and target
X = df[[
    "Temperature",
    "Weather",
    "Holiday",
    "Hour",
    "Day",
    "Month"
]]

y = df["Traffic_Volume"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=150,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred)
rmse = mean_squared_error(y_test, pred) ** 0.5
r2 = r2_score(y_test, pred)

print("=" * 50)
print("Random Forest Model")
print("=" * 50)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# Save model and encoders
joblib.dump(model, "model/traffic_model.pkl")
joblib.dump(weather_encoder, "model/weather_encoder.pkl")
joblib.dump(holiday_encoder, "model/holiday_encoder.pkl")

print("\n✅ Model saved successfully!")