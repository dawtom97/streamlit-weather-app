import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

excel_path = os.getenv("EXCEL_FILE_PATH")

st.set_page_config(page_title="Pogoda z OpenWeather", layout="wide")
st.caption("Dodatkowy opis")

@st.cache_data(ttl=20)
def load_data():
    if os.path.exists(excel_path):
        df = pd.read_excel(excel_path)
        return df
    else:
        return pd.DataFrame()

if st.button("Odśwież dane"):
    st.cache_data.clear()

st.spinner(text="Trwa ładowanie")

df = load_data()

if df.empty:
    st.warning("Brak danych pogodowych")
else:
    st.dataframe(df, use_container_width=True)

    latest = df.iloc[-1]

    st.subheader("Ostatnie dane")
    col1,col2,col3 = st.columns(3)
    col1.metric("Temperatura",f"{latest['temperature']}°C")
    col2.metric("Wilgotność", f"{latest['humidity']}%")
    col3.metric("Prędkość wiatru", f"{latest['wind_speed']} m/s")

    st.subheader("Wczytaj plik")

    uploaded_file = st.file_uploader("Wybierz plik", type=["xlsx","csv"])

    if uploaded_file is not None:
        df_file = pd.read_excel(uploaded_file)
        st.caption("Zawartość pliku")
        st.dataframe(df_file)
    else:
        st.info("Proszę wgrać plik Excel")

