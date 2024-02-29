import streamlit as st
st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️')

st.header("Consulta el estado de tu proceso jurídico 🔎")

col1, col2 = st.columns(2)

with col1:
    nombre = st.text_input('Ingrese el nombre del cliente de Novus Legal:', '''
    ''')

with col2:
    cedula =  st.text_input('Ingrese el número de cédula:', '''
    ''')


h = st.button('Revisar mi Caso en vivo con Novus Legal ⚖️')

if h:
    st.write('¡Cargando tu caso <<', nombre, '>>! En breve te compartiremos tu portal de monitoreo número<<', cedula, '>>')
