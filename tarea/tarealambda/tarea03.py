"""
3. Dada una lista de tuplas donde cada tupla contiene dos números, ordena la lista de
tuplas basándote en el segundo elemento de cada tupla utilizando la función sorted y
una función lambda
[(3, 5), (6, 2), (9, 7), (4, 1), (8, 6), (7, 3)]
"""
lista_de_tuplas = [(3, 5), (6, 2), (9, 7), (4, 1), (8, 6), (7, 3)]
lista_ordenada = sorted(lista_de_tuplas, key=lambda tupla: tupla[1])
print(lista_ordenada)
