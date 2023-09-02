"""
Escriba un programa en Python que realice las siguientes 9 multiplicaciones y muestre el
resultado de cada producto

1 * 1 = 1
11 * 11 = 121
111 * 111 = ?
1111 * 1111 = ?
...

1111111111 * 1111111111 = ?
"""
# Realizar las multiplicaciones y mostrar los resultados
# Realizar las multiplicaciones y mostrar los resultados
for i in range(1, 10):
    numero = int('1' * i)
    resultado = numero * numero
    print(f"{numero} * {numero} = {resultado}")
