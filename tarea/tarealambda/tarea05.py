'''
5. Escriba un programa para implementar una calculadora simple con operaciones de suma,
resta, multiplicación y división. Cada operación debe ser implementada utilizando una
función lambda. El usuario debe elegir una de las operaciones a realizar, o abandonar el
programa, seleccionada una de las operaciones debe solicitarle el ingreso de dos
números para realizar con ellos la operación seleccionada. La calculadora debe continuar
ejecutándose y pidiendo más operaciones hasta que el usuario decida salir.
'''
# Funciones lambda para las operaciones
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "Error: División por cero"

while True:
    # Mostrar el menú de opciones al usuario
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Solicitar la elección del usuario
    opcion = input("Elija una operación (1/2/3/4/5): ")

    # Salir si el usuario elige la opción 5
    if opcion == '5':
        print("¡Hasta luego!")
        break

    # Solicitar los números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación seleccionada y mostrar el resultado
    if opcion == '1':
        resultado = suma(num1, num2)
    elif opcion == '2':
        resultado = resta(num1, num2)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
    elif opcion == '4':
        resultado = division(num1, num2)
    else:
        resultado = "Opción no válida"

    print(f"Resultado: {resultado}\n")
