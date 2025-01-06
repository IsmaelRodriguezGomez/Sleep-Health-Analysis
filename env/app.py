import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Sleep Health and Lifestyle Analysis")

# Cargar el dataset (asegúrate de que el nombre coincida exactamente)
df = pd.read_csv("sleep_health_lifestyle_dataset.csv")

# Mostrar una vista previa de los datos
st.write("### Vista previa de los datos")
st.write(df.head())  # Muestra las primeras 5 filas

# Opcional: Muestra el número de filas y columnas
st.write("Este dataset tiene", df.shape[0], "filas y", df.shape[1], "columnas.")