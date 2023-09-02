"""
Escribir un programa que pida al usuario ingresar una oración, almacene internamente en
una lista cada una de las palabras de la oración, las palabras almacenadas no deben
contener espacios ni comas, ni puntos, luego pida al usuario que ingrese un número
entre 1 y 10, el programa debe devolver una lista con las palabras que tienen ese número
de caracteres.
"""

# Solicitar al usuario que ingrese una oración
oracion = input("Ingrese una oración: ")

# Dividir la oración en palabras y eliminar espacios, comas y puntos
palabras = oracion.split()
palabras = [palabra.strip(',.') for palabra in palabras]

# Solicitar al usuario que ingrese un número entre 1 y 10
while True:
    try:
        numero = int(input("Ingrese un número entre 1 y 10: "))
        if 1 <= numero <= 10:
            break
        else:
            print("Número fuera del rango permitido. Intente nuevamente.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Filtrar las palabras que tienen el número de caracteres especificado
palabras_con_numero_de_caracteres = [palabra for palabra in palabras if len(palabra) == numero]

# Mostrar la lista de palabras con ese número de caracteres
print(f"Palabras con {numero} caracteres: {', '.join(palabras_con_numero_de_caracteres)}")
