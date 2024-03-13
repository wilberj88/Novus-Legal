import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️ Legalización de Tierras 🗺️')

st.header("Experiente jurídico 🔎 #001-SAN-COL-2024")


col1, col2 = st.columns(2)
col1.write("Propietarios: Isbelia Hernández, Wilber Jiménez Viloria y Wilber Jiménez Hernández")
col1.write("Área: 42 hectáreas")
col1.write("Número de Matrícula Inmobiliario: _______")
col1.write("Número Predial: ______")

with col2:
  m = folium.Map(location=[6.9115957, -73.7144061], zoom_start=13)
  folium.Marker(
    [6.9115957, -73.7144061], popup="Predio El Porvenir", tooltip="Predio El Porvenir", icon=folium.Icon(icon='cloud')
    ).add_to(m)


st.subheader ("Etapas de legalización")
