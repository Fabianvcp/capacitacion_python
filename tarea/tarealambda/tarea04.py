"""
4. Dado un diccionario donde las claves son nombres de personas y los valores son sus
edades, utiliza un diccionario de comprensión y una función lambda para modificar el
diccionario de manera que las edades se incrementen en 1
{‘Miguel’: 20, ‘Norma’: 25, ‘Elizabeth’: 19, ‘Esteban’: 31, ‘Jorge’: 21}

"""
edades = {'Miguel': 20, 'Norma': 25, 'Elizabeth': 19, 'Esteban': 31, 'Jorge': 21}
edades_incrementadas = {nombre: edad + 1 for nombre, edad in edades.items()}
print(edades_incrementadas)
