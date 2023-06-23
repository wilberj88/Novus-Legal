import streamlit as st
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
from streamlit_timeline import st_timeline
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime
import base64
from pyecharts import options as opts
from pyecharts.charts import Graph


st.set_page_config(layout="wide", page_title="Novus Legal ⚖️", page_icon="⚖️")

st.title('Novus Legal ⚖️')

st.header("Tecnología Jurídica Para tu Asesoría y Defensa")

option = st.selectbox(
    '¿En cuál temática deseas que te apoyemos?',
    ('Familia', 'Procesal', 'Contractual'))

if option:
    st.write('Te apoyaremos en tu consulta en', option)

option1 = st.selectbox(
    '¿Cuál acompañamiento te queda mejor?',
    ('Asistentes Virtuales 🤖 desde $15.000 consulta', '👩‍⚖️ Abogados Especialistas🧑🏽‍⚖️ desde $100.000 consulta'))
if option1:
    st.write('Elegiste', option1)
