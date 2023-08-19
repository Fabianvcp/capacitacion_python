"""
Pide al usuario que ingrese un número y devuelve como resultado si ese número es par o
impar.
"""
def es_par(a):
    return a % 2 == 0

try:
    num = int(input('Ingresa un numero entero:\n'))
    
    if es_par(num):
        print(f'{num} es un numero par')
    else:
        print(f'{num} es un numero impar')

except ValueError:
    print("Error: ingresa solo número enteros.")
