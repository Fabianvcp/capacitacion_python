"""
Pide al usuario que introduzca un número. Luego, convierte ese número a float e imprime el
resultado.
"""

def numero1():
    while True:
        num_1 = input('Me puede decir su número?\n') 
        if num_1.isdigit() and num_1.isnumeric():
            return int(num_1)
        else:
            print("Por favor, ingrese una valor válido (represente un número entero).")

numero_1 = numero1()

print(f"su numero convertido en decimal es {float(numero_1)}")