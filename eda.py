import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Create images folder
# -----------------------------
os.makedirs("images", exist_ok=True)

# -----------------------------
# Professional Theme
# -----------------------------
sns.set_theme(style="whitegrid", palette="deep")

plt.rcParams["figure.figsize"] = (10,6)
plt.rcParams["figure.dpi"] = 300
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 13

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("dataset/traffic_dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])

df["Hour"] = df["Date"].dt.hour
df["Day"] = df["Date"].dt.day_name()
df["Month"] = df["Date"].dt.month_name()

print("Dataset Loaded Successfully")
print(df.head())

# =====================================
# Graph 1
# Average Traffic by Hour
# =====================================

plt.figure(figsize=(12,6))

hourly = df.groupby("Hour")["Traffic_Volume"].mean().reset_index()

sns.lineplot(
    data=hourly,
    x="Hour",
    y="Traffic_Volume",
    marker="o",
    linewidth=3
)

plt.title("Average Traffic Volume Throughout the Day")
plt.xlabel("Hour")
plt.ylabel("Traffic Volume")

plt.tight_layout()
plt.savefig("images/01_traffic_by_hour.png")
plt.close()

# =====================================
# Graph 2
# Weather Impact
# =====================================

plt.figure(figsize=(9,6))

weather = df.groupby("Weather")["Traffic_Volume"].mean().sort_values()

sns.barplot(
    x=weather.index,
    y=weather.values
)

plt.title("Average Traffic Volume by Weather")
plt.xlabel("Weather")
plt.ylabel("Traffic Volume")

plt.tight_layout()
plt.savefig("images/02_weather_effect.png")
plt.close()

# =====================================
# Graph 3
# Holiday Impact
# =====================================

plt.figure(figsize=(7,6))

holiday = df.groupby("Holiday")["Traffic_Volume"].mean()

plt.pie(
    holiday.values,
    labels=holiday.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Traffic Distribution: Holiday vs Non-Holiday")

plt.savefig("images/03_holiday_pie.png")
plt.close()

# =====================================
# Graph 4
# Temperature Distribution
# =====================================

plt.figure(figsize=(10,6))

sns.histplot(
    df["Temperature"],
    bins=20,
    kde=True
)

plt.title("Temperature Distribution")

plt.tight_layout()

plt.savefig("images/04_temperature_distribution.png")

plt.close()

# =====================================
# Graph 5
# Traffic Distribution
# =====================================

plt.figure(figsize=(10,6))

sns.histplot(
    df["Traffic_Volume"],
    bins=30,
    kde=True
)

plt.title("Traffic Volume Distribution")

plt.tight_layout()

plt.savefig("images/05_traffic_distribution.png")

plt.close()

# =====================================
# Graph 6
# Traffic by Day
# =====================================

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

daily = (
    df.groupby("Day")["Traffic_Volume"]
    .mean()
    .reindex(days)
)

plt.figure(figsize=(11,6))

sns.barplot(
    x=daily.index,
    y=daily.values
)

plt.title("Average Traffic by Day of Week")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("images/06_daywise_traffic.png")

plt.close()

# =====================================
# Graph 7
# Monthly Trend
# =====================================

monthly = df.groupby("Month")["Traffic_Volume"].mean()

plt.figure(figsize=(12,6))

plt.plot(
    monthly.index,
    monthly.values,
    marker="o",
    linewidth=3
)

plt.xticks(rotation=45)

plt.title("Monthly Average Traffic")

plt.tight_layout()

plt.savefig("images/07_monthly_trend.png")

plt.close()

# =====================================
# Graph 8
# Correlation Heatmap
# =====================================

corr = df.copy()

corr["Weather"] = corr["Weather"].astype("category").cat.codes
corr["Holiday"] = corr["Holiday"].astype("category").cat.codes

corr["Hour"] = corr["Date"].dt.hour
corr["Month"] = corr["Date"].dt.month

plt.figure(figsize=(8,6))

sns.heatmap(
    corr[
        [
            "Temperature",
            "Weather",
            "Holiday",
            "Hour",
            "Month",
            "Traffic_Volume"
        ]
    ].corr(),
    annot=True,
    cmap="Blues"
)

plt.title("Feature Correlation Heatmap")

plt.tight_layout()

plt.savefig("images/08_correlation_heatmap.png")

plt.close()

print("\n✅ All Professional Graphs Generated Successfully!")