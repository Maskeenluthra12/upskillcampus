from google import genai
import streamlit as st
import time

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


def ask_gemini(question):

    models = [
        "gemini-flash-latest",
        "gemini-2.0-flash",
        "gemini-2.5-flash"
    ]

    for model in models:

        for _ in range(3):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=question
                )

                return response.text

            except Exception as e:

                if "503" in str(e):
                    time.sleep(2)
                    continue

                if "404" in str(e):
                    break

                return f"Error: {e}"

    return "Gemini is currently busy. Please try again in a few minutes."