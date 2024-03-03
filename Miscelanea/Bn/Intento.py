from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
import streamlit as st

# He colocado la variable q en la construcción de q
# sin embargo, para evitar la inclusión de ese parámetro
# en las opciones dentro de streamlit
# Preferí luego establecer la sustitución q=1-p
# Eliminando así la necesidad de incluir otro valor.abs
# Note que esto a su vez simplifica el problema que 
# El usuario establezca un valor de q >1 

def binomial(x,n,p,q):
    comb = math.comb(n,x)
    p_x=p**x 
    q_nx= (q)**(n-x)
    return comb*p_x*q_nx

n=50
p=4/7
q=1-p

lista= np.arange(n+1)
data_table= pd.DataFrame({'x':lista})
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
print(data_table)
binomial_plot, axis =plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C1')

st.title('Gráficos Binomiales')
st.pyplot(binomial_plot)
