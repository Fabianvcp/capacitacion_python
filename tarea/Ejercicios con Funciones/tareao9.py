"""
Escribir una función que reciba como entrada dos oraciones (cadenas de texto) y
devuelva como salida una lista solamente con las palabras que están presentes en las dos
oraciones.
"""
def palabras_comunes(oracion1, oracion2):
    # Dividir las oraciones en palabras y convertirlas a minúsculas para evitar problemas de capitalización
    palabras_oracion1 = set(oracion1.lower().split())
    palabras_oracion2 = set(oracion2.lower().split())
    
    # Encontrar las palabras comunes en ambas oraciones
    palabras_comunes = list(palabras_oracion1.intersection(palabras_oracion2))
    
    return palabras_comunes

# Ejemplo de uso:
oracion1 = "Esta es una oración de ejemplo."
oracion2 = "Otra oración con palabras comunes y otras diferentes."
resultado = palabras_comunes(oracion1, oracion2)
print("Palabras comunes en las dos oraciones:", resultado)
