"""
    Pide al usuario que introduzca su nombre y su edad. Luego, imprime un mensaje que diga
    "Hola, [nombre]. Tienes [edad] años."
"""
def obtener_edad():
    while True:
        edad = input('Y me puede decir su edad?\n') 
        if edad.isdigit():
            if int(edad) < 150 and int(edad) > 0:
                return int(edad)
            else:
                print("El valor esta fuera de los valores permitidos")
        else:
            print("Por favor, ingrese una edad válida (represente un número).")
                   




nombre = input('Buenas, me puede decir cual es su nombre?\n')
edad = obtener_edad()

print(f'hola. {nombre}. Tienes {edad} años')