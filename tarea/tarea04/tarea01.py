"""
    Escriba un programa que encuentre todos los múltiplos de 5 menores que un valor dado:
    Ejemplo
    • Entrada: 36
    • Salida: 5 10 15 20 25 30 35
"""
# Pedir al usuario que ingrese un valor
valor_limite = int(input("Ingrese un valor: "))

# Utilizar un bucle for para encontrar y mostrar los múltiplos de 5
print("Múltiplos de 5 menores que", valor_limite, ":")

for i in range(5, valor_limite, 5):
    print(i, end=" ")

print()  # Imprimir una línea en blanco al final
