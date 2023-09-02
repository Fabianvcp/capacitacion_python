"""
Determine si un número dado es un número primo.
No es necesario implementar ningún algoritmo en concreto. La idea es probar los números
menores al dado e ir viendo si las divisiones tienen resto cero o no.
¿Podría optimizar su código? ¿Realmente es necesario probar con tantos divisores?
Ejemplo
• Entrada: 11
"""
import math

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    ## Limite es igual al cuadrado de numero + 1
    limite = int(math.sqrt(numero)) + 1
    
    for divisor in range(3, limite, 2):
        if numero % divisor == 0:
            return False
        return True

numero = 11

if es_primo(numero):
    print(f"{numero} es un número primo.")
else:    
    print(f"{numero} no es un número primo.")
