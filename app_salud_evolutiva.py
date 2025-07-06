
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="🩺 Evolución Clínica", layout="wide")
st.title("📈 Historial de Análisis Clínicos")

conn = sqlite3.connect("evolucion_clinica_salvador.db")
df = pd.read_sql_query("SELECT * FROM resultados_clinicos ORDER BY fecha ASC", conn)
conn.close()

st.dataframe(df, use_container_width=True)

parametro = st.selectbox("Selecciona un parámetro", df['parametro'].unique())
df_param = df[df['parametro'] == parametro]

st.line_chart(data=df_param, x='fecha', y='valor')
