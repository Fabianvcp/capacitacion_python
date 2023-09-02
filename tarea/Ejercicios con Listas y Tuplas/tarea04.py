"""
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por
pantalla en orden inverso separados por comas.
"""

# Crear una lista con los números del 1 al 10
numeros = list(range(1, 11))

# Revertir la lista
numeros_inversos = numeros[::-1]

# Convertir los números inversos a una cadena separada por comas
cadena_numeros_inversos = ', '.join(map(str, numeros_inversos))

# Mostrar la cadena de números inversos
print(cadena_numeros_inversos)
