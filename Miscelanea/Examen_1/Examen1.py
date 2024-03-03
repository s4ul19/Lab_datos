from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import math
import streamlit as st

st.title('Exámen 1')
st.write('El fin de esta aplicación realizar varias gráficas de distribuciones binomiales para valores de n que vayan de 0 a 100, incluí tambíen una tabla para que se pueda contamplar los datos tambíen, quiero enfatizar que los datos que salen como 0 son solo aproximaciones, pues el numero que reperesentan es bastante pequeño. Su uso es bastante fácil, solo introduzca valores de |n| <= 100 y valores de |p|<=1, darle click a almacenar datos y listo, tiene su gráfica ! ' )
st.write(' Los unicos widgets que usé fueron los del button, .write, y .number_input, consideré que ellos eran suficientes para cumplir con la funcionalidad adecuada del programa ')
n_0=1
p_0=0.5
# Se propone un boton...
boton = st.button("Haz clic para asignar valores")
# El boton nos permite activar las dos opciones para almacenar los datos escritos
# Note que la función que usé permite acotar las opciones

n = st.number_input("Ingresa el valor de n (Valor permitido de 0 a 100):", min_value=0, max_value=100, step=1, value=n_0)
p = st.number_input("Ingresa el valor de p (Valor permitido de 0 a 1):", min_value=0.0, max_value=1.0, step=0.01, value=p_0)

if boton:
    # Muestra los valores ingresados por el usuario
    st.write("El valor ingresado de n es:", n)
    st.write("El valor ingresado de p es:", p)

# He colocado la variable q en la construcción de la función
# sin embargo, para evitar la inclusión de ese parámetro
# en las opciones dentro de streamlit
# Preferí luego establecer la sustitución q=1-p
# Eliminando así la necesidad de incluir otro valor
# Note que esto a su vez simplifica el problema que 
# El usuario establezca un valor de q >1 
q=1-p
def binomial(x,n,p,q):
    comb = math.comb(n,x)
    p_x=p**x 
    q_nx= (q)**(n-x)
    return comb*p_x*q_nx
lista= np.arange(n+1)
data_table= pd.DataFrame({'x':lista})
# Esto denota la tabla a graficar y es la que aparece al final de la página
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
binomial_plot, axis =plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C1')

st.title('Gráficos Binomiales')
st.pyplot(binomial_plot)
st.write('Tabla de valores')
st.table(data_table['Pb'])
