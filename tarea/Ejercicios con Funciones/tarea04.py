#"Escribir una función que reciba una lista de números y devuelva su promedio."
def calcular_promedio(lista):
    if not lista:
        return None  # Manejo de lista vacía
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)

if promedio is not None:
    print(f"El promedio de la lista {numeros} es: {promedio}")
else:
    print("La lista está vacía.")
 