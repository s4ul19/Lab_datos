# file: streamlit_tests.py
# date: 05-02-2024

import streamlit as st
import plotly.express as px
import pandas as pd


# Agregar título a la página
st.title('Gráficas')

# Agregar texto a la página
st.write('Se toman en cuentan unicamente 3 especies')
# Leer datos de pinguinos como lo trabajado en el cuaderno
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
# Los prints solo serán visibles en la terminal pero no en la página de Streamlit.
print(data)
# Generar la gráfica a partir de los datos y guardarla en una variable llamada grafica.
grafica = px.scatter(data,'bill_depth_mm','flipper_length_mm','species',symbol='sex',)

# Agregar la gráfica a la página
st.plotly_chart(grafica)

