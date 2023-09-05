"""
Escribir una función que reciba un número entero positivo y devuelva su factorial.
"""

def factorial(n):
    if n < 0:
        return None  # Manejo de números negativos
    elif n == 0:
        return 1  # El factorial de 0 es 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso:
numero = int(input("ingrese un numero:\n"))
resultado = factorial(numero)
if resultado is not None:
    print(f"El factorial de {numero} es {resultado}")
else:
    print("Por favor, ingrese un número entero positivo.")
