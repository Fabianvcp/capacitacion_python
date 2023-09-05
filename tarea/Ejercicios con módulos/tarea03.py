"""
3. Cree dos archivos, uno calc.py que debe contener la definición de las funciones de suma,
resta, multiplicación, división, seno y coseno. Luego un segundo archivo main.py que
debe importar las funciones del archivo calc, y con ellas implementar una calculadora que
permita utilizar todas las funciones contenidas en el módulo calc
"""
import modulo

while True:
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Seno")
    print("6. Coseno")
    print("7. Salir")
    
    opcion = input("Seleccione una operación (1/2/3/4/5/6/7): ")
    
    if opcion == '7':
        break
    
    if opcion in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Ingrese el primer número: "))
        if opcion != '5' and opcion != '6':
            num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            resultado = calc.suma(num1, num2)
        elif opcion == '2':
            resultado = calc.resta(num1, num2)
        elif opcion == '3':
            resultado = calc.multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = calc.division(num1, num2)
        elif opcion == '5':
            resultado = calc.seno(num1)
        elif opcion == '6':
            resultado = calc.coseno(num1)
        
        print(f"Resultado: {resultado}")
    else:
        print("Opción no válida. Intente nuevamente.")
