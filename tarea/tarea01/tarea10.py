peso_its = 250
peso_barbie = 250

def its():
    while True:
        num_1 = input('Ingrese el numero de payasos vendidos:\n') 
        if num_1.isdigit():
            return int(num_1)
        else:
            print("Por favor, ingrese un valor de venta valido válida (represente un número).")

def barbie():
    while True:
        num_1 = input('Ingrese el numero de muñecas vendidas:\n') 
        if num_1.isdigit():
            return int(num_1)
        else:
            print("Por favor, ingrese un valor de venta valido válida (represente un número).")
            
muñeca = barbie()
payaso = its()

peso_total= (payaso * peso_its) + (muñeca * peso_its)

print(f'El peso total del paquete a enviar es: {peso_total}')
