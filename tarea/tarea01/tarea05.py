import math


def numero1():
    while True:
        num_1 = input('Me puede decir su número?\n') 
        if num_1.isdigit() or num_1.isnumeric():
            return float(int(num_1))
        else:
            print("Por favor, ingrese una numero válido (represente un número).")

def raiz_cuadrada(a):
    if a < 0:
        return print("Error: no se puede calcular la raiz cuadrada de un numero negativo.")
    return math.sqrt(a)

numero_1 = numero1()

print(f'Raiz cuadrada de {numero_1} es igual a {raiz_cuadrada(numero_1)}')