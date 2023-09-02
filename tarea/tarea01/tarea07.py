"""
Pide al usuario que introduzca su altura en metros y su peso en kilogramos. Luego, calcula e
imprime su índice de masa corporal (IMC).
"""

def peso():
    while True:
        num_1 = input('Me puede decir su peso en kilogramos?\n') 
        if num_1.isdigit():
            if float(num_1) < 0.0 or float(num_1) > 200.0 :
                print(f"el peso ingresado de {num_1} esta fuera de los parametros permitidos")
            else:
                return float(num_1)
        else:
            print("Por favor, ingrese un valor de peso válida (represente un número).")

def altura():
    while True:
        num_2 = input('Y me puede decir su altura en metros?\n') 
        if '.' in num_2:
                return float(num_2)
        else:
            if num_2.isnumeric() and int(num_2) > 0 and int(num_2)< 280:
                    return int(num_2)/100
            else:
                print('los valores ingresado no pueden ser procesado por el sistema')
        

def imc(kg, mtrs):
    return kg / (mtrs ** 2)

kg = peso()
mtrs = altura()

print(f'El indice de masa corporla correspondiente a los valores de un peso{kg} y una altura de {mtrs} es de: {imc(kg,mtrs)}')
