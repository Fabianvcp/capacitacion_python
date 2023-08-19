"""
11. Cree un programa que calcule las raíces x1 y x2 de una expresión cuadrática:

2x² + 3x − 5 = 0

Utilice la fórmula de Baskara.
x = −b ± √b2 − 4ac/2a

12. Verifique que las raíces encontradas en el punto anterior resuelven realmente la ecuación
dada.
"""
import math

def raiz_cuadrada(a,b,c):
    baskara = b**2 - 4*a*c

    if baskara < 0:
        return None #no hay raices reales
    else:
        x1 = (-b + math.sqrt(baskara))/(2*a)
        x2 = (-b - math.sqrt(baskara))/(2*a)
        return x1,x2

a = 2
b = 3
c = -5

raices = raiz_cuadrada(a,b,c)

if raices is None:
    print("No hay raices para esta ecuación")
else:
    x1,x2 = raices
    print(f"Las raíces x1 y x2 son: {x1:.2f} y {x2: .2f}")
