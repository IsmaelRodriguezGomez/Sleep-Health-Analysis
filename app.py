import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el dataset
df = pd.read_csv("sleep_health_lifestyle_dataset.csv")

# Título de la aplicación
st.title("Sleep Health and Lifestyle Analysis")
st.write("""
    En esta aplicación, exploramos cómo el estrés, la actividad física y otros factores de estilo de vida afectan la salud del sueño.
    Utilizamos gráficos interactivos para analizar la duración del sueño y su relación con otras variables.
""")

# Mostrar el DataFrame
st.write("### Vista previa de los datos")
st.dataframe(df)

# Mostrar el número de filas y columnas
st.write(f"Este dataset tiene {df.shape[0]} filas y {df.shape[1]} columnas.")

# Histograma de la duración del sueño
if st.button("Mostrar Histograma de Duración de Sueño"):
    fig = px.histogram(df, x="Sleep Duration (hours)", title="Histograma de Duración del Sueño")
    st.write("Histograma de Horas de Sueño")
    st.plotly_chart(fig)

# Gráfico de dispersión (Sueño vs Estrés)
if st.button("Mostrar Dispersión (Sueño vs. Estrés)"):
    fig2 = px.scatter(df, x="Sleep Duration (hours)", y="Stress Level (scale: 1-10)", 
                      title="Gráfico de Dispersión entre Horas de Sueño y Nivel de Estrés")
    st.write("Gráfico de Dispersión entre Horas de Sueño y Nivel de Estrés")
    st.plotly_chart(fig2)

# Gráfico de barras (Estrés vs Calidad del Sueño)
if st.button("Mostrar Distribución del Estrés por Calidad de Sueño"):
    fig3 = px.bar(df, x="Quality of Sleep (scale: 1-10)", y="Stress Level (scale: 1-10)",
                  title="Distribución del Estrés por Calidad de Sueño")
    st.write("Distribución del Estrés por Calidad de Sueño")
    st.plotly_chart(fig3)

# Dispersión entre sueño y actividad física
if st.button("Mostrar Dispersión (Sueño vs Actividad Física)"):
    fig4 = px.scatter(df, x="Sleep Duration (hours)", y="Physical Activity Level (minutes/day)", 
                      title="Sueño vs Actividad Física")
    st.write("Gráfico de Dispersión entre Horas de Sueño y Actividad Física")
    st.plotly_chart(fig4)

# Gráfico de dispersión sin líneas para Duración del Sueño vs Calidad del Sueño
st.write("### Comparación de Duración del Sueño vs Calidad del Sueño (Dispersión sin líneas)")
plt.figure(figsize=(10,6))
plt.scatter(df["Sleep Duration (hours)"], df["Quality of Sleep (scale: 1-10)"], color='b')
plt.title("Duración del Sueño vs. Calidad del Sueño")
plt.xlabel("Duración del Sueño (horas)")
plt.ylabel("Calidad del Sueño")
st.pyplot(plt)

# Gráfico de cajas (boxplot) para Duración del Sueño vs Calidad del Sueño
st.write("### Comparación de Duración del Sueño vs Calidad del Sueño (Boxplot)")
plt.figure(figsize=(10,6))
sns.boxplot(x="Quality of Sleep (scale: 1-10)", y="Sleep Duration (hours)", data=df, palette="Blues")
plt.title("Duración del Sueño vs. Calidad del Sueño")
plt.xlabel("Calidad del Sueño")
plt.ylabel("Duración del Sueño (horas)")
st.pyplot(plt)

# Agregar un filtro interactivo para comparar datos por calidad de sueño
quality_filter = st.selectbox("Filtrar por Calidad de Sueño", df["Quality of Sleep (scale: 1-10)"].unique())
filtered_data = df[df["Quality of Sleep (scale: 1-10)"] == quality_filter]

st.write(f"### Datos filtrados por calidad de sueño ({quality_filter})")
st.dataframe(filtered_data)

# Agregar una tabla con estadísticas descriptivas
st.write("### Estadísticas Descriptivas del Dataset")
st.write(df.describe())

# Agregar análisis de correlación entre Duración del Sueño y Nivel de Estrés
correlation = df["Sleep Duration (hours)"].corr(df["Stress Level (scale: 1-10)"])
st.write(f"### Correlación entre Duración del Sueño y Nivel de Estrés: {correlation:.2f}")
if abs(correlation) > 0.3:
    st.write("Existen indicios de una relación moderada entre la duración del sueño y el nivel de estrés.")
else:
    st.write("No hay una relación significativa entre la duración del sueño y el nivel de estrés.")

# Filtro interactivo para seleccionar un rango de horas de sueño y calcular la media del nivel de estrés
st.write("### Filtrar por rango de horas de sueño")
min_sleep, max_sleep = st.slider(
    "Selecciona el rango de horas de sueño",
    min_value=int(df["Sleep Duration (hours)"].min()),  # Asegúrate de que esto sea un entero
    max_value=int(df["Sleep Duration (hours)"].max()),  # Asegúrate de que esto sea un entero
    value=(int(df["Sleep Duration (hours)"].min()), int(df["Sleep Duration (hours)"].max())),
    step=1  # Esto hace que el paso sea un valor entero
)

# Filtrar los datos por el rango de horas de sueño seleccionado
filtered_data_sleep = df[(df["Sleep Duration (hours)"] >= min_sleep) & (df["Sleep Duration (hours)"] <= max_sleep)]

# Calcular la media del nivel de estrés para el rango seleccionado
average_stress = filtered_data_sleep["Stress Level (scale: 1-10)"].mean()

# Mostrar la media del nivel de estrés
st.write(f"### Media del nivel de estrés para las horas de sueño seleccionadas: {average_stress:.2f}")

# Crear un gráfico de barras que muestre la media del estrés
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(["Media del Nivel de Estrés"], [average_stress], color='skyblue')

# Añadir etiquetas
ax.set_xlabel("Nivel de Estrés (Promedio)")
ax.set_title(f"Media de Estrés para {min_sleep}-{max_sleep} horas de Sueño")
ax.set_xlim(0, 10)  # Nivel máximo de estrés (escala de 1-10)

# Mostrar el gráfico
st.pyplot(fig)

# Filtro interactivo por nivel de estrés
st.write("### Filtrar por nivel de estrés")
min_stress, max_stress = st.slider(
    "Selecciona el rango de nivel de estrés",
    min_value=1, 
    max_value=10,
    value=(1, 10),
    step=1
)

# Filtrar los datos por el rango de estrés seleccionado
filtered_data_stress = df[(df["Stress Level (scale: 1-10)"] >= min_stress) & (df["Stress Level (scale: 1-10)"] <= max_stress)]

# Mostrar los datos filtrados
st.write(f"### Datos filtrados por nivel de estrés entre {min_stress} y {max_stress}")
st.dataframe(filtered_data_stress)

# Consejos para mejorar la calidad del sueño
st.write("""
    ### Consejos para mejorar la calidad del sueño:
    - Mantén un horario de sueño regular.
    - Realiza actividad física durante el día.
    - Evita el uso de pantallas antes de dormir.
    - Practica técnicas de relajación para reducir el estrés.
""")
