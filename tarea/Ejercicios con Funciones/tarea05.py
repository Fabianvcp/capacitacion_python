"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un
cilindro usando la primera función.
"""

import math

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    if radio < 0:
        return None  # Manejo de radio negativo
    area = math.pi * radio**2
    return area

# Función para calcular el volumen de un cilindro utilizando la función de área de círculo
def calcular_volumen_cilindro(radio, altura):
    if radio < 0 or altura < 0:
        return None  # Manejo de valores negativos
    area_base = calcular_area_circulo(radio)
    if area_base is None:
        return None  # Manejo de radio negativo en la función de área de círculo
    volumen = area_base * altura
    return volumen

# Ejemplo de uso:
radio_circulo = 5
altura_cilindro = 10

area_circulo = calcular_area_circulo(radio_circulo)
volumen_cilindro = calcular_volumen_cilindro(radio_circulo, altura_cilindro)

if area_circulo is not None and volumen_cilindro is not None:
    print(f"Área del círculo con radio {radio_circulo}: {area_circulo}")
    print(f"Volumen del cilindro con radio {radio_circulo} y altura {altura_cilindro}: {volumen_cilindro}")
else:
    print("Por favor, ingrese valores no negativos para el radio y la altura.")
