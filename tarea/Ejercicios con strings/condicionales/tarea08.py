"""
Escriba un programa que pida un la introducción de un año con un valor entero, compruebe
si dicho año es bisiesto o no lo es. Un año es bisiesto en el calendario Gregoriano, si es
divisible entre 4 y no divisible entre 100, o bien si es divisible entre 400. Puedes hacer la
comprobación en esta lista de años bisiestos.
Ejemplo
• Introduzca un año: 2008
• Salida: Es un año bisiesto
"""

año = int(input("Introduzca un año: "))
es_bisiesto=  año % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if (year):
    print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.")