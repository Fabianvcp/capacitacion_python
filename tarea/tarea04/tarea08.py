"""
Escriba un programa que calcule el máximo común divisor entre dos números enteros.
No utilice ningún algoritmo existente. Hágalo probando divisores.
Ejemplo
• Entrada: a=12; b=44
• Salida: 4
"""
# Función para calcular el máximo común divisor (MCD) de dos números
def calcular_mcd(a, b):
    # Encontrar el menor de los dos números
    if a < b:
        menor = a
    else:
        menor = b
    
    # Iniciar el MCD en 1
    mcd = 1
    
    # Probar todos los posibles divisores desde 1 hasta el menor de los dos números
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0:
            mcd = i
    
    return mcd

# Pedir al usuario que ingrese dos números enteros
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

# Calcular el MCD utilizando la función
mcd = calcular_mcd(a, b)

# Mostrar el resultado
print(f"El máximo común divisor (MCD) de {a} y {b} es: {mcd}")
