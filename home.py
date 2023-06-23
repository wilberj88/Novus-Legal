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

st.header("Consultas Jurídicas 🔍 y Defensa de Derechos Vulnerados 👊")
st.write("Tenemos Asistentes Virtuales 🤖 Expertos en Temáticas Jurídicas y 👩‍⚖️ Abogados Especialistas🧑🏽‍⚖️ para atención y acompañamiento humano")

st.write("Define tu consulta:")

tab1, tab2, tab3, tab4 = st.tabs(["Familia", "Suceciones", "Impugnaciones de Paternidad o Maternindad", "Procesal"])
