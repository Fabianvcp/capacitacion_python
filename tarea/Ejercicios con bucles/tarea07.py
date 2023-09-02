"""
Escriba un programa que calcule la distancia hamming entre dos cadenas de texto de la
misma longitud
Ejemplo
• Entrada: 0001010011101 y 0000110010001
• Salida: 4
"""

# Solicitar al usuario que ingrese las dos cadenas de texto
cadena1 = input("Ingrese la primera cadena de texto: ")
cadena2 = input("Ingrese la segunda cadena de texto: ")

# Verificar si las cadenas tienen la misma longitud
if len(cadena1) != len(cadena2):
    print("Las cadenas no tienen la misma longitud.")
else:
    # Calcular la distancia de Hamming
    distancia = sum(c1 != c2 for c1, c2 in zip(cadena1, cadena2))
    print(f"La distancia de Hamming entre las cadenas es: {distancia}")

