"""
11. Escriba un programa que imprima el siguiente patrón de caracteres:
0000000000
0011111100
0022111100
0022221100
0022222200
0000000000
"""
# Tamaño del patrón
filas = 6
columnas = 10

# Inicializar una lista vacía para representar el patrón
patron = []

# Llenar la lista con ceros iniciales
for _ in range(filas):
    patron.append([0] * columnas)

# Llenar el patrón con los valores requeridos
for fila in range(filas):
    for columna in range(fila + 1):
        patron[fila][columna] = fila

# Imprimir el patrón
for fila in patron:
    print(''.join(map(str, fila)))
