""" Escribir un programa que pregunte el nombre el un producto, su precio y un número de
unidades y muestre por pantalla una cadena con el nombre del producto seguido de su
precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y
el coste total con 8 dígitos enteros y 2 decimales """

nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio unitario del producto: "))
unidades = int(input("Ingrese el número de unidades: "))

precio_unitario = "{:07.2f}".format(precio)
costo_total = "{:07.2f}".format(precio * unidades)

print(f"Nombre del producto: {nombre}")
print(f"Precio unitario: {precio_unitario}")
print(f"Número de unidades: {unidades}")
print(f"Costo total: {costo_total}")
