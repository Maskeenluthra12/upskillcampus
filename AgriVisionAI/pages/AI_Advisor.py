import streamlit as st
from services.gemini_service import ask_gemini

st.set_page_config(
    page_title="AI Advisor",
    page_icon="🤖",
    layout="wide"
)

st.title("AgriVision AI Advisor")

question = st.text_area(
    "Your Question",
    placeholder="Example: Which crop is best for Punjab in July?"
)

st.write("Question received:", question)

if st.button("Ask AI"):

    st.write("Button Clicked!")

    answer = ask_gemini(question)

    st.code(answer)