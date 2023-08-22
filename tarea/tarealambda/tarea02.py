"""
2. Dada una lista de números enteros (puede ser fija o ingresada manualmente), usa la
función map y una función lambda para crear una nueva lista que contenga solo los
números pares de la lista original.
"""
numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
numeros_pares = list(map(lambda x: x if x % 2 == 0 else None, numeros))
numeros_pares = list(filter(lambda x: x is not None, numeros_pares))

print(numeros_pares)
