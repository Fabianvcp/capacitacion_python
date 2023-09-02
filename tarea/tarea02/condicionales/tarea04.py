# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par
# o impar

def es_par(numero):
    return numero % 2 == 0

try:
    numero = int(input("Ingrese un número entero: "))
    if es_par(numero):
        print("El número es par.")
    else:
        print("El número es impar.")
except ValueError:
    print("Error: Ingrese un número entero válido.")