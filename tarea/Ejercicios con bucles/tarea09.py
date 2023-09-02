"""
Escriba un programa que calcule el valor de x para el que la función f(x) = x
2 − 6x + 3
obtiene su menor resultado. Centre la búsqueda en el rango [−9] a [9], para simplificar
utilice sólo valores enteros.
• El resultado es: x = 3 y f(3) = −6
"""

import matplotlib.pyplot as plt
import numpy as np

# Definir la función f(x)
def f(x):
    return x**2 - 6*x + 3

# Generar valores de x en el rango [-9, 9]
x = np.linspace(-9, 9, 400)

# Calcular los valores correspondientes de f(x)
y = f(x)

# Encontrar el mínimo y su posición
x_minimo = 3
y_minimo = f(x_minimo)

# Crear el gráfico
plt.plot(x, y, label='f(x) = x^2 - 6x + 3')
plt.scatter(x_minimo, y_minimo, color='red', label=f'Minimo en x={x_minimo}, f({x_minimo})={y_minimo}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico de f(x)')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()
