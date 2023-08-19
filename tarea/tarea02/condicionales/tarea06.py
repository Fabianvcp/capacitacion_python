"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $400
y si es mayor de 18 años, $900.
"""

edad = int(input("Ingrese la edad del cliente: "))

if edad.isdigit():
    if edad < 4:
        print("El cliente puede entrar gratis.")
    elif 4 <= edad <= 18:
        print(f"El precio de la entrada es: $400")
    else:
        print(f"El precio de la entrada es: $900")
else:    
    print("Error: Ingrese una edad válida (número entero).")
    
