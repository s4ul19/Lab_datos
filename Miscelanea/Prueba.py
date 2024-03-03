import streamlit as st
import plotly.express as px 
import pandas as pd

st.title('Test Streamlit')
st.write('Alguna cosa')
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
grafica = px.scatter(data,'bill_length_mm','bill_depth_mm','species',symbol='sex',)
st.plotly_chart(grafica)
