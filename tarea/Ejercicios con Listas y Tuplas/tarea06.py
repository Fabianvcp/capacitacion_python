"""
Escribir un programa que pida al usuario que ingrese números, guárdelos en una lista
hasta que el usuario ingrese el 0, entonces imprima los valores guardados en la lista de
mayor a menor.
"""
# Inicializar una lista para almacenar los números
numeros = []

# Solicitar al usuario que ingrese números y agregarlos a la lista
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    
    if numero == 0:
        break
    
    numeros.append(numero)

# Ordenar la lista en orden descendente
numeros.sort(reverse=True)

# Mostrar los números en orden descendente
print("Números en orden descendente:")
for numero in numeros:
    print(numero, end=' ')
