"""
Escribir un programa que determine si una cadena de texto dada es un heterograma, o
no, es decir, no se repite ninguna letra.
Ejemplos de heterogramas
• yuxtaponer
• centrifugado
• cerveza
• junio
"""

def es_heterograma(cadena):
    # Convertir la cadena a minúsculas para considerar mayúsculas y minúsculas iguales
    cadena = cadena.lower()
    
    # Crear un conjunto para almacenar letras únicas
    letras_vistas = set()
    
    for letra in cadena:
        # Si la letra ya ha sido vista, no es un heterograma
        if letra in letras_vistas:
            return False
        # Agregar la letra al conjunto de letras vistas
        letras_vistas.add(letra)
    
    # Si se ha recorrido toda la cadena sin repetir letras, es un heterograma
    return True

# Pedir al usuario que ingrese una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Verificar si es un heterograma
if es_heterograma(cadena):
    print("Es un heterograma.")
else:
    print("No es un heterograma.")
