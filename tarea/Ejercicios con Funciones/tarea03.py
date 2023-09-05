"""
Escriba una función en Python que reciba una lista de valores enteros y devuelva otra lista
sólo con aquellos valores pares.
Ejemplo:
Entrada: [1, 3, 4, 8, 9, 10, 11, 13, 15, 18, 22, 27, 32, 35]
Salida: [4, 8, 10, 18, 22, 32]
"""

def obtener_pares(lista):
    pares = [x for x in lista if x % 2 == 0]
    return pares

# Ejemplo de uso:
entrada = [1, 3, 4, 8, 9, 10, 11, 13, 15, 18, 22, 27, 32, 35]
pares = obtener_pares(entrada)
print("Entrada:", entrada)
print("Salida:", pares)
