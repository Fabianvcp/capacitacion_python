"""
Pide al usuario que introduzca dos números. Imprime el valor y el tipo de dato de cada
número.
"""
def numero1():
    while True:
        num_1 = input('Me puede decir su primer número?\n') 
        if num_1.isdigit():
            return int(num_1)
        else:
            print("Por favor, ingrese una edad válida (represente un número).")

def numero2():
    while True:
        num_2 = input('Y me puede decir su segundo número?\n') 
        if num_2.isdigit():
            return int(num_2)
        else:
            print("Por favor, ingrese una edad válida (represente un número).")

numero_1 = numero1()
numero_2 = numero2()

print(f"El primer número es {numero_1} y su tipo {type(numero_1)}\nEl segundo número es {numero_2} y si su tipo {type(numero_2)}")