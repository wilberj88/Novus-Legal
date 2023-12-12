import streamlit as st
import pandas as pd
import numpy as np
import datetime
import base64
import streamlit.components.v1 as com
from streamlit_gsheets import GSheetsConnection



st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

#ConnectGoogleSheet

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(worksheet="Solicitudes")
data = data.dropna(how="all")
existing_data = data


st.title('Novus Legal ⚖️ & Corpojurídicos')

st.header("Tecnología Jurídica Para tu Asesoría y Defensa")

TEMATICAS_JURIDICAS = [
    "Familia - Sucesiones",
    "Familia - Divorcios",
    "Procesal - Civil - Legalización de Predios",
    "Procesal - Comercial",
    "Procesal - Penal",
    "Contractual - Contratos de Trabajo",
    "Contractual - Contratos de Obra",
    "Contractual - Contratos de Prestación de Servicios",
    "Contractual - Contratos de Arriendo",
    "Otra",
]

SERVICIOS = [
    "Consulta Jurídica - Abogado Virtual - Desde 15.000$",
    "Consulta Jurídica - Abogado Especialista - Desde 100.000$"
]

RESPUESTAS = [
    "Videollamada",
    "Correo Electrónico con respuesta en texto",
    "Audio explicativo"
]

tematica = st.selectbox(
    '¿En cuál temática jurídica necesitas que te apoyemos?', 
    options=TEMATICAS_JURIDICAS, 
    index=None
)



servicio = st.selectbox(
    '¿Cuál acompañamiento jurídico te queda mejor?', 
    options=SERVICIOS, 
    index=None)

if tematica and servicio:
    st.write('Te apoyaremos en tu consulta en', tematica)
    st.write('Para el servicio de ', servicio)
    st.subheader('Por favor diligencia el formulario para preparar la respuesta a tu consulta ⚖️')
    with st.form(key="user_form"):
        user_name = st.text_input(label="Nombre y Apellido*")
        user_email = st.text_input(label="Correo")
        user_consult = st.text_area(label="¿Cuál es tu consulta? Por favor enlista todas tus preguntas")
        user_respuesta = st.selectbox(
            '¿Cómo prefieres la respuesta a tu consulta?', 
            options=RESPUESTAS, 
            index=None)
        
        submit_button = st.form_submit_button(label="Cargar Consulta")
        
        # If the submit button is pressed
        if submit_button:
            # Check if all mandatory fields are filled
            if not user_name or not user_email or not user_consult:
                st.warning("Diligencia todos los espacios por favor")
                st.stop()
            else:
                # Create a new row of user data
                new_user_data = pd.DataFrame(
                    [
                        {
                            "User_Nombre": user_name,
                            "User_Correo": user_email,
                            "User_Consulta": user_consult,
                            "User_Tematica": tematica,
                            "User_Servicio": servicio,
                        }
                    ]
                )
                st.dataframe(new_user_data)
                updated_df = pd.concat([existing_data, new_user_data], ignore_index=True)
                conn.update(worksheet="Solicitudes", data=updated_df)
                st.success("Formulario cargado")
                st.subheader("Paga tu consulta y recibe respuesta en menos de 24h") 
                com.html("""
                <script type='text/javascript' src='https://storage.ko-fi.com/cdn/widget/Widget_2.js'></script><script type='text/javascript'>kofiwidget2.init('Pagar Consulta', '#29abe0', 'Q5Q8S0K6H');kofiwidget2.draw();</script> 
                """)
