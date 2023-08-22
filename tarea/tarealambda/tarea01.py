"""
Escriba un programa que realice el cálculo de la superficie de un círculo dado su radio,
para implementarlo utilice una función lambda.
"""
superficie_circulo = lambda radio: 3.14159 * radio**2
radio = float(input("Ingrese el radio del círculo: "))
superficie = superficie_circulo(radio)
print(f"La superficie del círculo con radio {radio} es {superficie:.2f}")
