"""
Escribir un programa que pregunte al usuario los números que conforman el billete
ganador del quini6, los almacene en una lista y los muestre por pantalla ordenados de
menor a mayor.
"""
# Solicitar al usuario los números y almacenarlos en una lista
billete_ganador = []

while True:
    numero = input("Ingrese un número del billete ganador (o 'fin' para terminar): ")
    
    if numero.lower() == 'fin':
        break
    
    try:
        numero = int(numero)
        billete_ganador.append(numero)
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Ordenar la lista de números de menor a mayor
billete_ganador.sort()

# Mostrar los números ordenados
print("Números del billete ganador ordenados de menor a mayor:")
for numero in billete_ganador:
    print(numero, end=' ')

print()  # Imprimir una línea en blanco al final
