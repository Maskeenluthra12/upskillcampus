import requests
import streamlit as st

API_KEY = st.secrets["WEATHER_API_KEY"]


def get_weather(city):
    url = (
        f"http://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city}&aqi=yes"
    )

    try:
        response = requests.get(url)

        if response.status_code != 200:
            st.error(response.json().get("error", {}).get("message", "Unknown error"))
            return None

        data = response.json()

        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "wind": data["current"]["wind_kph"],
            "pressure": data["current"]["pressure_mb"],
            "description": data["current"]["condition"]["text"],
            "icon": "https:" + data["current"]["condition"]["icon"],
            "feels_like": data["current"]["feelslike_c"],
            "uv": data["current"]["uv"]
        }
    

    except Exception as e:
        st.error(str(e))
        return None
    st.image(weather["icon"], width=90)
    