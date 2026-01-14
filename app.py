import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

st.header("🚗 Análisis de anuncios de venta de vehículos")

st.write("""
Esta aplicación web permite explorar un conjunto de datos de anuncios de vehículos usados en Estados Unidos
mediante visualizaciones interactivas.
""")

st.subheader("📊 Visualizaciones interactivas")
st.write("Selecciona las casillas para generar los gráficos correspondientes:")

# Checkbox para histograma
build_histogram = st.checkbox("Construir histograma")

if build_histogram:
    st.subheader("Distribución del kilometraje")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribución del kilometraje de los vehículos"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para scatter
build_scatter = st.checkbox("Construir gráfico de dispersión")

if build_scatter:
    st.subheader("Relación precio vs kilometraje")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Precio vs Kilometraje"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
