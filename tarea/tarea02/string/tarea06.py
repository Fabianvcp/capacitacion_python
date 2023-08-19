""" Escriba un programa en Python que acepte un entero n y compute el valor de n + nn + nnn
o Entrada: 5
o Salida: 615 (5 + 55 + 555) """

entrada = input("Ingrese un numero entero:\n")

if entrada.isdigit() and int(entrada) >= 0 and len(entrada) == 1:
    uno = int(entrada)
    dos = int(entrada) * 11
    tres = int(entrada) * 111
    salida = uno + dos + tres
    print(f"el resultado es {salida}")
else:
    print("El valor ingresado es incorrecto")    