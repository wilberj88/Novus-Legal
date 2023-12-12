import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
from streamlit_timeline import st_timeline
import plotly.express as px
import pandas as pd
import numpy as np
import datetime
import base64
from pyecharts import options as opts
from pyecharts.charts import Graph


st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️ & Corpojurídicos')

st.header("Tecnología Jurídica Para tu Asesoría y Defensa")

TEMATICAS_JURIDICAS = [
    "Familia - Sucesiones",
    "Familia - Divorcios",
    "Procesal",
    "Contractual",
    "Otra",
]

SERVICIOS = [
    "Consulta Jurídica - Abogado Virtual - Desde 15.000$",
    "Consulta Jurídica - Abogado Especialista - Desde 100.000$"
]

tematica = st.selectbox(
    '¿En cuál temática jurídica necesitas que te apoyemos?', 
    options=TEMATICAS_JURIDICAS)

if option:
    st.write('Te apoyaremos en tu consulta en', tematica)

servicio = st.selectbox(
    '¿Cuál acompañamiento jurídico te queda mejor?', options=SERVICIOS)
if option1:
    st.write('Elegiste', option1)


with st.form(key="user_form"):
    user_name = st.text_input(label="User Name*")
    user_email = st.text_input(label="User Email*")
    user_love = st.text_area(label="¿Qué te divierte? No te aburrirías de hacerlo casi todos los días")
    user_good = st.text_area(label="¿Para qué eres bueno? Agrega link de Linkedin del Rol al que aspiras")
    user_paid = st.multiselect("Por qué te pagarían", options=PAIDS)
    user_world_needs = st.selectbox("ODS que te mueve*", options=ODS, index=None)
    

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit New User Details")

    # If the submit button is pressed
    if submit_button:
        # Check if all mandatory fields are filled
        if not user_name or not user_email:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        elif existing_data["User_Name"].str.contains(user_name).any():
            st.warning("A user with this name already exists.")
            st.stop()
        else:
            # Create a new row of vendor data
            new_user_data = pd.DataFrame(
                [
                    {
                        "User_Name": user_name,
                        "User_Email": user_email,
                        "User_Love": user_love,
                        "User_Good": user_good,
                        "User_Paid": user_paid,
                        "User_World_Needs": user_world_needs,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, new_user_data], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(worksheet="Users", data=updated_df)

            st.success("User details successfully submitted! Bienvenido a MandIki")
