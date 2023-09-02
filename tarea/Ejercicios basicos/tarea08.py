""" 
Pide al usuario la medida de la base y la altura de un triángulo, luego calcula y muestra su
superficie.
"""
def base():
    while True:
        num_1 = input('Me puede decir el valor de la base del tringualo:\n')
        if num_1.isdigit() or float(num_1) > 0.0:
            return float(num_1)
        else:
            print("ingrese valores dentro los parametros que permite el sistema")

def altura():
        while True:
            num_2 = input('Ingrese el la altura del triangulo:\n')
            if num_2.isdigit() or float(num_2) > 0.0:
                return float(num_2)
            else:
                print('Ingrese valores dentro de los parametros que el sistema puede procesar')

def superficie(a,b):
    total = (a*b)/2


numero_1 = base()
numero_2 = altura()

print(f'La superficie de la altura de {numero_2} y una base de {numero_1} es de {superficie(numero_1,numero_2)}')            