"""
Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el
saludo ¡Hola <nombre>!.
"""

def saludo(nombre):
    print(f'Hola {nombre}')


n = input("Por favor ingrese su nombre")

saludo(n)