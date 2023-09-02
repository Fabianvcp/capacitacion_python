"""
User
Escriba un programa que muestre (por filas) la Tabla ASCII, empezando con el código 33
y terminando con el 127, Tal como se muestra en la siguiente imagen.
"""
# Inicializar el código de inicio y fin de la tabla ASCII
inicio = 33
fin = 127

# Número de columnas por fila
columnas_por_fila = 10

# Inicializar contador de columnas
columna_actual = 0

# Recorrer los códigos ASCII y mostrar los caracteres en filas
for codigo in range(inicio, fin + 1):
    caracter = chr(codigo)
    print(f"{codigo}: {caracter}", end="\t")
    columna_actual += 1
    
    # Cambiar de fila cada 'columnas_por_fila' columnas
    if columna_actual == columnas_por_fila:
        print()  # Cambiar de fila
        columna_actual = 0

# Imprimir una línea en blanco al final
print()
