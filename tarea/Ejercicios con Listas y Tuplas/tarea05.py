"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número
de veces que contiene cada vocal.
"""

# Pedir al usuario que ingrese una palabra
palabra = input("Ingrese una palabra: ")

# Inicializar contadores para cada vocal
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

# Recorrer la palabra y contar cada vocal
for letra in palabra:
    if letra.lower() == 'a':
        cont_a += 1
    elif letra.lower() == 'e':
        cont_e += 1
    elif letra.lower() == 'i':
        cont_i += 1
    elif letra.lower() == 'o':
        cont_o += 1
    elif letra.lower() == 'u':
        cont_u += 1

# Mostrar los conteos de cada vocal
print(f"Número de 'a's en la palabra: {cont_a}")
print(f"Número de 'e's en la palabra: {cont_e}")
print(f"Número de 'i's en la palabra: {cont_i}")
print(f"Número de 'o's en la palabra: {cont_o}")
print(f"Número de 'u's en la palabra: {cont_u}")

