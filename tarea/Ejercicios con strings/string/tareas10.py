""" Escriba un programa en Python que acepte una palabra en castellano y calcule una métrica
que sea el número total de caracteres de la palabra multiplicado por el número total de
vocales que contiene la palabra.
o Entrada: ordenador
o Salida: 36 """


palabra = input("Ingrese una palabra en castellano: ")

caracteres = len(palabra)

vocales = sum(1 for letra in palabra if letra.lower () in 'aeiou')

metrica = caracteres * vocales

print(type(vocales))

print(f'El resultado es {metrica}')