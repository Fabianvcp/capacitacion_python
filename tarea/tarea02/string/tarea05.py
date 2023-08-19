""" 
Escriba un programa en Python que acepte un «string» con los 8 dígitos de un NIF, y calcule
su dígito de control
o Entrada: 12345678
o Salida: 12345678Z
"""
def calcular_digital_control(n):
    letras_control = "TRWAGMYFPDXBNJZSQVHLCKE"
    indice = int(n)% 23
    letras_control = letras_control[indice]
    
    return + letras_control

n = input("Ingrese los 8 digitos del NIF:\n")

resultado= calcular_digital_control(n)

print(resultado)    