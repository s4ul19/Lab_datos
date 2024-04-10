import numpy as np
import matplotlib.pyplot as plt

# Definir la función escalar en función de r
def scalar_function(r):
    # Función dada: f(r) = 4r
    return 4 * r

# Generar valores de r y theta
r_values = np.linspace(0, 10, 100)
theta_values = np.linspace(0, 2*np.pi, 100)

# Crear una malla de valores de r y theta
r, theta = np.meshgrid(r_values, theta_values)

# Calcular los valores de la función escalar en la malla
scalar_values = scalar_function(r)

# Crear el gráfico polar
plt.figure()
plt.contourf(r * np.cos(theta), r * np.sin(theta), scalar_values, cmap='viridis')
plt.colorbar(label='Valor de la función escalar')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curvas de nivel de la función potencial ')
plt.show()
