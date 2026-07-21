import streamlit as st

st.set_page_config(page_title="Crop Prediction",layout="wide")

st.title("Crop Prediction")

state=st.selectbox(
    "State",
    [
        "Punjab",
        "Karnataka",
        "Tamil Nadu",
        "Kerala",
        "Maharashtra"
    ]
)

season=st.selectbox(
    "Season",
    [
        "Kharif",
        "Rabi",
        "Whole Year"
    ]
)

rainfall=st.number_input("Rainfall (mm)",0.0)

temperature=st.number_input("Temperature (°C)",0.0)

if st.button("Predict"):

    st.success("Predicted Crop : Rice")

    st.metric("Estimated Production","3.8 Tons/Hectare")