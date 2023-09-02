"""Escriba un programa que acepte 3 números y calcule el máximo, el mínimo y el
promedio.
Ejemplo
• Entrada: 7, 4, 9
• Salida: max=9, min=4, prom=6.66"""

def calcular_max_min_promedio(num1, num2, num3):
    maximo = max(num1, num2, num3)
    minimo = min(num1, num2, num3)
    promedio = (num1 + num2 + num3) / 3
    return maximo, minimo, promedio

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    maximo, minimo, promedio = calcular_max_min_promedio(num1, num2, num3)

    print(f"max={maximo}, min={minimo}, prom={promedio:.2f}")
except ValueError:
    print("Error: Ingrese números válidos.")
