import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️ Legalización de Tierras 🗺️')

st.header("Experiente jurídico 🔎 #001-SAN-COL-2024")


col1, col2 = st.columns(2)
col1.subheader("Propietarios:")
col1.write("Isbelia Hernández, Wilber Jiménez Viloria y Wilber Jiménez Hernández")
col1.subheader("Área")
col1.write("42 hectáreas")
col1.subheader("Número de Matrícula Inmobiliario:")
col1.write("303-61779")
col1.subheader("Código Catastral:")
col1.write("680810002000000040125000000000COD")

with col2:
  m = folium.Map(location=[6.9115957, -73.7144061], zoom_start=13)
  folium.Marker(
    [6.9115957, -73.7144061], popup="Predio El Porvenir", tooltip="Predio El Porvenir", icon=folium.Icon(icon='cloud')
    ).add_to(m)
  st_data = st_folium(m, width=250)



st.subheader ("Etapas de legalización")
