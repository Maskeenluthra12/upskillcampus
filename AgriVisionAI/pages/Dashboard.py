import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard")

st.write("### Platform Statistics")

c1,c2,c3,c4=st.columns(4)

c1.metric("Crops","120+")
c2.metric("States","28")
c3.metric("Accuracy","96%")
c4.metric("Farmers","10K+")

st.divider()

df=pd.DataFrame({
    "Year":[2019,2020,2021,2022,2023],
    "Production":[120,132,145,158,172]
})

fig = px.line(
    df,
    x="Crop_Year",
    y="Production",
    color_discrete_sequence=["#2E7D32"]
)

st.plotly_chart(fig,use_container_width=True)