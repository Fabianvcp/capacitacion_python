""" Escribir un programa que pregunte por consola por los productos de una compra en un
almacén, los productos deben ingresarse indicando la cantidad, dos puntos y el nombre del
producto, luego cada producto separado por comas, al final el programa debe mostrar por
pantalla cada uno de los productos en una línea distinta, indicando su cantidad.
o Ingrese productos: 6:huevos, 1:azúcar, 4:latas de pescado
o Salida:

        6 huevos
        1 azúcar
        4 latas de pescado """

def mostrar_productos(productos):
    for producto in productos:
        cantidad, nombre = producto.split(":")
        print(f"{cantidad.strip()} {nombre.strip()}")
        
p_input = input("Ingrese los productos separados por comas (formato: cantidad:nombre): ")

productos = p_input.split(",")

print("Salida:")
mostrar_productos(productos)
