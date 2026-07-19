# ==========================================================
# UrbanFlow AI Enterprise Edition v5.0
# Smart City Traffic Intelligence Dashboard
# ==========================================================


import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

from datetime import datetime
import base64
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="UrbanFlow AI",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

if os.path.exists("assets/style.css"):
    with open("assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

# --------------------------------------------------
# LOAD HERO IMAGE
# --------------------------------------------------

def get_base64(path):
    try:
        with open(path, "rb") as img:
            return base64.b64encode(img.read()).decode()
    except:
        return ""

hero = get_base64("assets/hero.jpg")

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

DATASET_PATH = "dataset/traffic_dataset.csv"

if os.path.exists(DATASET_PATH):
    df = pd.read_csv(DATASET_PATH)
else:
    st.error("Dataset not found.")
    st.stop()

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

MODEL_PATH = "model/traffic_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    st.error("Model not found.")
    st.stop()

# --------------------------------------------------
# LOAD ENCODERS
# --------------------------------------------------

weather_encoder = joblib.load("model/weather_encoder.pkl")
holiday_encoder = joblib.load("model/holiday_encoder.pkl")

# ==================================================
# HERO SECTION
# ==================================================

st.markdown(
    f"""
<div class="hero"
style="background-image:url('data:image/jpeg;base64,{hero}')">

<div class="hero-content">

<div class="hero-title">
🌆 UrbanFlow AI
</div>

<div class="hero-sub">
Enterprise Smart City Traffic Intelligence Platform
</div>

<br>

<span class="hero-chip">
🟢 SYSTEM ONLINE
</span>

<br><br>

<h4 style="color:white;">
{datetime.now().strftime("%d %B %Y | %I:%M %p")}
</h4>

</div>

</div>
""",
unsafe_allow_html=True
)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.image("assets/logo.png", use_container_width=True)

st.sidebar.title("⚙ Control Center")

city = st.sidebar.selectbox(
    "🏙 Select City",
    [
        "Delhi",
        "Mumbai",
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Kolkata"
    ]
)

temperature = st.sidebar.slider(
    "🌡 Temperature (°C)",
    0,
    50,
    28
)

weather = st.sidebar.selectbox(
    "🌦 Weather",
    list(weather_encoder.classes_)
)

holiday = st.sidebar.selectbox(
    "🎉 Holiday",
    list(holiday_encoder.classes_)
)

hour = st.sidebar.slider(
    "🕒 Hour",
    0,
    23,
    8
)

day = st.sidebar.selectbox(
    "📅 Day",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
)

month = st.sidebar.slider(
    "📆 Month",
    1,
    12,
    7
)

predict = st.sidebar.button(
    "🚦 Predict Traffic",
    use_container_width=True
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 AI Model Ready")

st.sidebar.info(f"""
**Current City**

📍 {city}

🕒 {datetime.now().strftime("%H:%M")}

🤖 Enterprise Edition
""")

# ==================================================
# DASHBOARD TITLE
# ==================================================

st.markdown("## 📊 Smart City Command Center")
