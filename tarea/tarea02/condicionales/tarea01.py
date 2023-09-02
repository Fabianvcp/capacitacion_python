""" Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de
edad o no """

edad = input("Ingrese su edad:\n")

if edad.isdigit() and int(edad) >= 18:
    print("Sos mayor de edad")
else:
    print("No sos mayor de edad")