""" Escribir un programa que almacene internamente la cadena de caracteres ‘password ‘ en
una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. """

contraseña = 'password'

repetir = input("ingrese le contraseña:\t")

if contraseña.lower() == repetir.lower():
    print("la contraseña coincide con la almacenada")
else:
    print("Error Contraseña erronea")