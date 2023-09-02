"""
Escribir un programa que pida el ingreso de 5 palabras en minúsculas, pidiéndolas una
por vez, guarde esas palabras en una lista, al completar el ingreso de las 5 palabras cree
otra lista utilizando lista de comprensión con las mismas palabras, pero en mayúsculas.
Imprima esta última lista por pantalla.
"""
# Solicitar al usuario el ingreso de 5 palabras en minúsculas
palabras = []
for i in range(5):
    palabra = input("Ingrese una palabra en minúsculas: ")
    palabras.append(palabra)

# Crear otra lista con las mismas palabras en mayúsculas utilizando lista de comprensión
palabras_en_mayusculas = [palabra.upper() for palabra in palabras]

# Imprimir la lista de palabras en mayúsculas
print("Palabras en mayúsculas:")
print(palabras_en_mayusculas)
