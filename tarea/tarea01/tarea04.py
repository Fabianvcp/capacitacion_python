"""
    Pide al usuario que ingrese dos números, realizar las operaciones básicas entre ellos e
    imprime los resultados:
    a. Suma
    b. Resta
    c. Multiplicación
    d. División
    e. División Entera
    f. Módulo
    g. Potencia
"""
def numero1():
    while True:
        num_1 = input('Me puede decir su primer número?\n') 
        if num_1.isdigit() or num_1.isnumeric():
            return float(int(num_1))
        else:
            print("Por favor, ingrese una numero válido (represente un número).")

def numero2():
    while True:
        num_2 = input('Y me puede decir su segundo número?\n') 
        if float(num_2) > 0:
            return float(int(num_2))
        else:
            print("Por favor, ingrese una numero válido (represente un número).")



def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no es válida."
    return a / b

def division_entera(a, b):
    if b == 0:
        return "Error: División por cero no es válida."
    return int(a) // int(b)

def modulo(a, b):
    if b == 0:
        return "Error: División por cero no es válida."
    return a % b

def potencia(a, b):
    return a ** b

# Pedimos al usuario que ingrese los dos números
try:
    
    numero_1 = numero1()
    numero_2 = numero2()
    
    # Realizamos las operaciones y mostramos los resultados
    print(f'Suma: {suma(numero_1, numero_2)}')
    print(f'Resta: {resta(numero_1, numero_2)}')
    print(f'Multiplicación: {multiplicacion(numero_1, numero_2)}')
    print(f'División: {division(numero_1, numero_2)}')
    print(f'División Entera: {division_entera(numero_1, numero_2)}')
    print(f'Módulo: {modulo(numero_1, numero_2)}')
    print(f'Potencia: {potencia(numero_1, numero_2)}')

except ValueError:
    print("Error: Ingresa solo números válidos.")

