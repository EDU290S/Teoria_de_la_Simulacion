import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros
P0 = 100  # Población inicial
r = 0.05  # Tasa de crecimiento

# Función de crecimiento
def growth(P, t):
    return r * P

# Tiempo de simulación
t = np.linspace(0, 10, 100)

# Simulación
P = odeint(growth, P0, t)

# Visualización
plt.plot(t, P)
plt.xlabel('Tiempo (años)')
plt.ylabel('Población')
plt.title('Crecimiento de la población de conejos')
plt.show()
