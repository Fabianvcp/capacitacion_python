"""
Escriba un programa que encuentre la mínima secuencia de múltiplos de 3 (distintos)
cuya suma sea igual o inferior a un valor dado.
Ejemplo
• Entrada: 45
• Salida: 0, 3, 6, 9, 12, 15
"""
# Pedir al usuario que ingrese un valor
valor_limite = int(input("Ingrese un valor: "))

# Inicializar variables
suma = 0
numero = 0
secuencia = []

# Encontrar la mínima secuencia de múltiplos de 3 cuya suma sea igual o inferior al valor dado
while suma <= valor_limite:
    secuencia.append(numero)
    suma += numero
    numero += 3

# Imprimir la secuencia
print("Mínima secuencia de múltiplos de 3 cuya suma es igual o inferior a", valor_limite, ":")
print(", ".join(map(str, secuencia)))
