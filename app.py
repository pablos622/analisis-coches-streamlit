import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análisis de anuncios de autos usados en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv')

if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma del odómetro de los vehículos')
    fig = px.histogram(car_data, x='odometer', nbins=30, title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión precio vs. año'):
    st.write('Relación entre precio y año del vehículo')
    fig2 = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año del modelo', opacity=0.5)
    st.plotly_chart(fig2, use_container_width=True)
