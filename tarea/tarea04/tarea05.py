"""
    Escriba un programa en Python que acepte dos cadenas de texto y compute el producto
    cartesiano letra a letra entre ellas.
    Ejemplo
    • Entrada: str1=abc; str2=123
    • Salida: a1 a2 a3 b1 b2 b3 c1 c2 c3
"""

# Pedir al usuario que ingrese las dos cadenas de texto
str1 = input("Ingrese la primera cadena de texto: ")
str2 = input("Ingrese la segunda cadena de texto: ")

# Calcular el producto cartesiano letra a letra
producto_cartesiano = [f"{c1}{c2}" for c1 in str1 for c2 in str2]

# Mostrar el resultado
print("Producto Cartesiano:")
print(" ".join(producto_cartesiano))
