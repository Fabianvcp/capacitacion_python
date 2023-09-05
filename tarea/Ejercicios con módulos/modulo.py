# calc.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero."

def seno(angulo):
    import math
    return math.sin(math.radians(angulo))

def coseno(angulo):
    import math
    return math.cos(math.radians(angulo))
