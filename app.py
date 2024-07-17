import pandas as pd
import plotly.express as px
import streamlit as st
        
st.title('Análisis de Vehículos')

car_data = pd.read_csv('vehicles_usa.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    

# Función para mostrar gráfico de distribución de años de modelo
def show_model_year_distribution():
    fig = px.histogram(car_data, x='model_year', title='Distribución de Años de Modelo', labels={'model_year': 'Año del Modelo'})
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig)

# Función para mostrar gráfico de dispersión (Kilometraje vs Precio)
def show_scatter_plot():
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Relación entre Kilometraje y Precio', labels={'odometer': 'Kilometraje', 'price': 'Precio'}, trendline='ols')
    st.plotly_chart(fig_scatter)

# Botón para mostrar gráfico de distribución de años de modelo
if st.button('Mostrar Distribución de Años de Modelo'):
    show_model_year_distribution()

# Botón para mostrar gráfico de dispersión (Kilometraje vs Precio)
if st.button('Mostrar Gráfico de Dispersión (Kilometraje vs Precio)'):
    show_scatter_plot()
