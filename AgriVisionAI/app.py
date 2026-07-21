import streamlit as st
import base64
import pandas as pd
import plotly.express as px

from services.weather_service import get_weather


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================================
# LOAD CSS
# =====================================================

with open("assets/css/style.css", "r") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# =====================================================
# LOAD HERO IMAGE
# =====================================================

def get_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

hero = get_base64("assets/images/hero.jpg")

# =====================================================
# HERO SECTION
# =====================================================

st.markdown(
f"""
<div class="hero"
style="background-image:url('data:image/jpg;base64,{hero}')">

<div class="overlay">

<div class="navbar">

<div class="logo">
AgriVision AI
</div>

<div class="menu">

<a href="#">Home</a>

<a href="#">Features</a>

<a href="#">Dashboard</a>

<a href="#">Weather</a>

<a href="#">AI Advisor</a>

<a href="#">Analytics</a>

</div>

<div class="nav-btn">

Smart Farming

</div>

</div>

<div class="hero-content">

<h1>AgriVision AI</h1>

<h2>
AI Powered Smart Agriculture Platform
</h2>

<p>
Predict • Analyze • Monitor • Grow
</p>

</div>

</div>

</div>

""",
unsafe_allow_html=True,
)

st.write("")
st.write("")

# =====================================================
# PLATFORM STATISTICS
# =====================================================

st.markdown(
"""
<h2 class="section-title">
Platform Statistics
</h2>
""",
unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Crops Supported", "120+")

with c2:
    st.metric("States Covered", "28")

with c3:
    st.metric("Prediction Accuracy", "96%")

with c4:
    st.metric("Farmers Benefited", "10K+")

st.write("")
st.write("")
# =====================================================
# FEATURES
# =====================================================

st.markdown(
"""
<h2 class="section-title">
What AgriVision AI Can Do
</h2>

<p class="section-subtitle">
Artificial Intelligence • Machine Learning • Weather Intelligence • Data Analytics
</p>
""",
unsafe_allow_html=True
)

st.write("")

# =====================================================
# FIRST ROW
# =====================================================

col1, col2, col3 = st.columns(3)

# ---------------- Crop Prediction ----------------

with col1:

    with st.container(border=True):

        st.subheader("Crop Prediction")

        st.write(
            """
Predict future crop production using Machine Learning
models trained on historical agricultural datasets.
            """
        )

        if st.button(
            "Open Crop Prediction",
            use_container_width=True,
            key="crop_prediction",
        ):
            st.switch_page("pages/Crop_Prediction.py")

# ---------------- Dashboard ----------------

with col2:

    with st.container(border=True):

        st.subheader("Dashboard")

        st.write(
            """
Explore production trends, charts and
interactive agricultural dashboards.
            """
        )

        if st.button(
            "Open Dashboard",
            use_container_width=True,
            key="dashboard",
        ):
            st.switch_page("pages/Dashboard.py")

# ---------------- Weather ----------------

with col3:

    with st.container(border=True):

        st.subheader("Weather")

        st.write(
            """
Monitor live temperature, humidity,
wind speed and weather conditions.
            """
        )

        if st.button(
            "Open Weather",
            use_container_width=True,
            key="weather",
        ):
            st.switch_page("pages/4_Weather.py")

st.write("")

# =====================================================
# SECOND ROW
# =====================================================

col4, col5, col6 = st.columns(3)

# ---------------- AI Advisor ----------------

with col4:

    with st.container(border=True):

        st.subheader("AI Advisor")

        st.write(
            """
Ask Gemini AI for crop recommendations,
farming guidance and expert advice.
            """
        )

        if st.button(
            "Open AI Advisor",
            use_container_width=True,
            key="advisor",
        ):
            st.switch_page("pages/AI_Advisor.py")

# ---------------- Advanced Analytics ----------------

with col5:

    with st.container(border=True):

        st.subheader("Advanced Analytics")

        st.write(
            """
Analyze production trends using
interactive charts and state-wise insights.
            """
        )

        if st.button(
            "Open Analytics",
            use_container_width=True,
            key="analytics",
        ):
            st.switch_page("pages/Advanced_Analytics.py")

# ---------------- Reports ----------------

with col6:

    with st.container(border=True):

        st.subheader("Reports")

        st.write(
            """
Generate AI-powered agricultural
reports and download them instantly.
            """
        )

        if st.button(
            "Open Reports",
            use_container_width=True,
            key="reports",
        ):
            st.switch_page("pages/Reports.py")

st.write("")
st.write("")
# =====================================================
# PRODUCTION TRENDS
# =====================================================

st.markdown(
"""
<h2 class="section-title">
Production Trends
</h2>

<p class="section-subtitle">
Agricultural Production Growth Over the Years
</p>
""",
unsafe_allow_html=True
)

data = pd.DataFrame(
    {
        "Year": [2019, 2020, 2021, 2022, 2023, 2024],
        "Production": [210, 228, 246, 268, 291, 318],
    }
)

fig = px.area(
    data,
    x="Year",
    y="Production",
    markers=True,
    color_discrete_sequence=["#2E7D32"]
)

fig.update_layout(
    template="plotly_white",
    height=450,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Year",
    yaxis_title="Production (Million Tonnes)",
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")
st.write("")

# =====================================================
# LIVE WEATHER
# =====================================================

st.markdown(
"""
<h2 class="section-title">
Live Weather Preview
</h2>

<p class="section-subtitle">
Real-time weather information powered by WeatherAPI
</p>
""",
unsafe_allow_html=True
)

city = st.text_input(
    "Enter City",
    value="Delhi",
    key="home_city",
)

weather = get_weather(city)

if weather:

    st.success(
        f"Current Weather in {weather['city']}, {weather['country']}"
    )

    w1, w2, w3, w4 = st.columns(4)

    with w1:
        st.metric(
            "Temperature",
            f"{weather['temperature']} °C"
        )

    with w2:
        st.metric(
            "Humidity",
            f"{weather['humidity']} %"
        )

    with w3:
        st.metric(
            "Wind Speed",
            f"{weather['wind']} km/h"
        )

    with w4:
        st.metric(
            "Pressure",
            f"{weather['pressure']} mb"
        )

    c1, c2 = st.columns([1, 4])

    with c1:
        st.image(weather["icon"], width=90)

    with c2:

        st.markdown(
            f"""
### {weather['description']}

**Feels Like:** {weather['feels_like']} °C

**UV Index:** {weather['uv']}
"""
        )

else:

    st.warning(
        "Unable to fetch weather information."
    )

st.write("")
st.write("")

# =====================================================
# AI ASSISTANT
# =====================================================

st.markdown(
"""
<h2 class="section-title">
AI Farming Assistant
</h2>

<p class="section-subtitle">
Get intelligent agricultural guidance powered by Google Gemini AI.
</p>
""",
unsafe_allow_html=True
)

st.write("")

left, center, right = st.columns([1, 2, 1])

with center:

    st.info(
        """
### AgriVision AI can help you with:

• Crop Recommendations

• Fertilizer Suggestions

• Pest & Disease Management

• Weather-Based Farming Advice

• Irrigation Planning

• Government Agricultural Schemes

Click below to start chatting with the AI Advisor.
"""
    )

    if st.button(
        "Open AI Advisor",
        use_container_width=True,
        key="homepage_ai",
    ):
        st.switch_page("pages/AI_Advisor.py")

st.write("")
st.write("")

# =====================================================
# ABOUT
# =====================================================

st.markdown(
"""
<h2 class="section-title">
About AgriVision AI
</h2>

<p class="about-text">

AgriVision AI is an intelligent agriculture platform that combines
Artificial Intelligence, Machine Learning, Weather Intelligence,
Data Analytics and Interactive Visualizations to support farmers,
researchers and policymakers in making smarter agricultural decisions.

The platform provides crop prediction, weather monitoring,
AI-powered recommendations, advanced analytics and automated
report generation to improve productivity and sustainability.

</p>
""",
unsafe_allow_html=True
)

st.write("")
st.write("")

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.markdown(
"""
<h2 class="section-title">
Technology Stack
</h2>

<p class="section-subtitle">
Core technologies powering AgriVision AI
</p>
""",
unsafe_allow_html=True
)

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.container(border=True)
    st.markdown(
        """
### Frontend

- Streamlit
- HTML
- CSS
"""
    )

with tech2:
    st.container(border=True)
    st.markdown(
        """
### AI & ML

- Google Gemini
- Scikit-learn
- Pandas
- NumPy
"""
    )

with tech3:
    st.container(border=True)
    st.markdown(
        """
### APIs

- WeatherAPI
- Gemini API
"""
    )

with tech4:
    st.container(border=True)
    st.markdown(
        """
### Visualization

- Plotly
- Python
- Interactive Charts
"""
    )

st.write("")
st.write("")

# =====================================================
# QUICK ACCESS
# =====================================================

st.markdown(
"""
<h2 class="section-title">
Quick Access
</h2>
""",
unsafe_allow_html=True
)

q1, q2, q3, q4 = st.columns(4)

with q1:
    if st.button("Crop Prediction", use_container_width=True):
        st.switch_page("pages/Crop_Prediction.py")

with q2:
    if st.button("Weather", use_container_width=True):
        st.switch_page("pages/4_Weather.py")

with q3:
    if st.button("Analytics", use_container_width=True):
        st.switch_page("pages/Advanced_Analytics.py")

with q4:
    if st.button("Reports", use_container_width=True):
        st.switch_page("pages/Reports.py")

st.write("")
st.write("")

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:25px;">

<h2 style="color:#2E7D32;">
AgriVision AI
</h2>

<p style="font-size:18px;color:#666;">
Smart Agriculture Intelligence Platform
</p>

<p style="color:#888;">
Built using Streamlit • Google Gemini • WeatherAPI • Plotly • Machine Learning
</p>

<p style="color:#999;font-size:14px;">
© 2026 AgriVision AI | Empowering Smart Agriculture through Artificial Intelligence
</p>

</div>
""",
unsafe_allow_html=True
)