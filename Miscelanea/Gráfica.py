import numpy as np
import matplotlib.pyplot as plt

# Definir la función vectorial en coordenadas esféricas
def vector_function(r, theta, phi):
    # Calcular las componentes cartesianas del vector
    x = 3 * np.sin(theta) * np.cos(phi) / r**2
    y = 3 * np.sin(theta) * np.sin(phi) / r**2
    z = 3 * np.cos(theta) / r**2
    
    return x, y, z

# Generar valores de r, theta y phi
r_values = np.linspace(0.1, 5, 100)
theta_values = np.linspace(0, np.pi, 100)
phi_values = np.linspace(0, 2*np.pi, 100)

# Crear una malla de valores de r, theta y phi
r, theta, phi = np.meshgrid(r_values, theta_values, phi_values, indexing='ij')

# Calcular las componentes del vector en cada punto de la malla
x, y, z = vector_function(r, theta, phi)

# Graficar las componentes del vector en función de r
plt.figure()
plt.plot(r_values, x[:, 0, 0], label='Componente x')
plt.plot(r_values, y[:, 0, 0], label='Componente y')
plt.plot(r_values, z[:, 0, 0], label='Componente z')
plt.xlabel('r')
plt.ylabel('Componentes del vector')
plt.title('Componentes del vector F(r) en función de r')
plt.legend()
plt.grid(True)
plt.show()
