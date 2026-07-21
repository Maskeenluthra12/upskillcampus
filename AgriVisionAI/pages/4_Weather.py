import streamlit as st
from services.weather_service import get_weather
from services.gemini_service import ask_gemini

st.set_page_config(
    page_title="Weather",
    page_icon="🌦",
    layout="wide"
)

st.title("🌦 Weather Intelligence")

st.write("Get real-time weather and AI farming advice.")

city = st.text_input(
    "Enter City",
    placeholder="Delhi"
)

if st.button("Get Weather", use_container_width=True):

    weather = get_weather(city)

    if weather is None:

        st.error("City not found.")

    else:

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Temperature",
            f"{weather['temperature']} °C"
        )

        col2.metric(
            "Humidity",
            f"{weather['humidity']} %"
        )

        col3.metric(
            "Wind",
            f"{weather['wind']} km/h"
        )

        col4.metric(
            "Pressure",
            f"{weather['pressure']} hPa"
        )

        st.info(weather["description"])

        prompt = f"""

You are an agricultural expert.

Weather:

City: {weather['city']}

Temperature: {weather['temperature']}°C

Humidity: {weather['humidity']}%

Wind Speed: {weather['wind']} km/h

Condition: {weather['description']}

Give practical farming advice in bullet points.

"""

        advice = ask_gemini(prompt)

        st.subheader("🤖 AI Farming Advice")

        st.success(advice)