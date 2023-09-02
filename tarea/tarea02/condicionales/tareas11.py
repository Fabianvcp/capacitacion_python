"""
Escriba un programa que acepte edad, peso, pulso, tensión y plaquetas, y determine si
una persona cumple con estos requisitos para donar sangre.
• Entrada:

Ingrese los siguientes datos:
edad: 34
peso: 81
pulsaciones: 70
tensión (baja-alta en mmHg): 80-120
plaquetas: 150000
• Salida: Apto para donar sangre

"""

def es_apto_para_donar_sangre(edad, peso, pulsaciones, tension_baja, tension_alta, plaquetas):
    if edad >= 18 and edad <= 65:
        if peso >= 50 and pulsaciones >= 60 and pulsaciones <= 100:
            if tension_baja >= 70 and tension_baja <= 100 and tension_alta >= 110 and tension_alta <= 150:
                if plaquetas >= 150000:
                    return True
    return False

try:
    edad = int(input("Ingrese su edad: "))
    peso = float(input("Ingrese su peso (kg): "))
    pulsaciones = int(input("Ingrese su pulso por minuto: "))
    tension_baja, tension_alta = map(int, input("Ingrese su tensión (baja-alta en mmHg): ").split('-'))
    plaquetas = int(input("Ingrese su cantidad de plaquetas: "))

    if es_apto_para_donar_sangre(edad, peso, pulsaciones, tension_baja, tension_alta, plaquetas):
        print("Apto para donar sangre.")
    else:
        print("No apto para donar sangre.")
except ValueError:
    print("Error: Ingrese datos válidos.")
