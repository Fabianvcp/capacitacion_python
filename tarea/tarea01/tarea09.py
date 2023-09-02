""" 
User
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

def inversion():
    while True:
        num_1 = float(input('Me puede decir inicial de la inversion:\n'))
        if float(num_1) > 0.0:
            return float(num_1)
        else:
            print("ingrese valores dentro los parametros que permite el sistema")

def interes():
    while True:
        num_1 = float(input('Me puede decir el valor del interes anual:\n'))
        if float(num_1) > 0.0:
            return float(num_1)
        else:
            print("ingrese valores dentro los parametros que permite el sistema")

def tiempo():
    while True:
        num_1 = int(input('Me puede decir la cantidad de años que durará la inversion el dinero:\n'))
        if int(num_1) > 0:
            return float(num_1)
        else:
            print("ingrese valores dentro los parametros que permite el sistema")

def calcular(dinero,porcentaje,anios):
    return dinero * (1 + porcentaje/100)**anios


dinero = inversion()
porcentaje = interes()
anios = tiempo()

capital = calcular(dinero,porcentaje,anios)

print(f'El capital obtenido es de :{capital}')