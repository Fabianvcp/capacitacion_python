"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un
mensaje informando de ello.

Fruta Precio
Banana 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70
"""

# Crear un diccionario con los precios de las frutas
precios_frutas = {
    'Banana': 1.35,
    'Manzana': 0.80,
    'Pera': 0.85,
    'Naranja': 0.70
}

# Solicitar al usuario la fruta y la cantidad en kilos
fruta = input("Ingrese el nombre de la fruta: ")
kilos = float(input("Ingrese la cantidad en kilos: "))

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:
    print(f"La fruta {fruta} no está en el diccionario.")
