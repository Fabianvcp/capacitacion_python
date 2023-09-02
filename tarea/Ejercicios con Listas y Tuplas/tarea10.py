"""
Escribir un programa que pida el ingreso de 2 vectores de 4 elementos separados por
comas. Usted debe almacenarlos en 2 tuplas, realizar su producto escalar y mostrarlo por
pantalla. Recuerde que el producto escalar es la suma de los productos de cada
componente homóloga, por ejemplo: (2, 4, 6, 8).(1, 3, 5, 7) = 2*1 + 4*3 + 6*5 + 8*7 = 100
Ejemplo:
Ingrese vector 1: 2, 4, 6, 8
Ingrese vector 2: 1, 3, 5, 7
El producto escalar es: 100
"""

# Solicitar al usuario el ingreso de los dos vectores
vector1 = input("Ingrese el primer vector de 4 elementos separados por comas: ")
vector2 = input("Ingrese el segundo vector de 4 elementos separados por comas: ")

# Dividir los elementos de los vectores y convertirlos a enteros
elementos_vector1 = [int(x) for x in vector1.split(',')]
elementos_vector2 = [int(x) for x in vector2.split(',')]

# Verificar que ambos vectores tengan 4 elementos
if len(elementos_vector1) == 4 and len(elementos_vector2) == 4:
    # Calcular el producto escalar
    producto_escalar = sum(x * y for x, y in zip(elementos_vector1, elementos_vector2))
    
    # Mostrar el resultado
    print("El producto escalar es:", producto_escalar)
else:
    print("Ambos vectores deben tener exactamente 4 elementos.")
