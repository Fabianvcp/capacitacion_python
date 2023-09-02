"""
User
Escriba un programa que permita al usuario adivinar un número entero entre 0 y 100.
Indicar en cada intento si el número buscado es menor o mayor que el que se está
preguntando y mostrar igualmente el número de intentos hasta encontrar el número
objetivo.
Ejemplo
Introduzca número: 50
Mayor
Introduzca número: 100
Menor
Introduzca número: 90
Menor
Introduzca número: 87
Correcto! Has encontrado el número en 4 intentos
"""

import random

# Generar un número aleatorio entre 0 y 100
numero_objetivo = random.randint(0, 100)

intentos = 0
adivinado = False

print("Adivina el número entre 0 y 100.")

while not adivinado:
    try:
        intento = int(input("Introduce un número: "))
        intentos += 1

        if intento < numero_objetivo:
            print("Mayor")
        elif intento > numero_objetivo:
            print("Menor")
        else:
            print(f"¡Correcto! Has encontrado el número en {intentos} intentos.")
            adivinado = True
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

