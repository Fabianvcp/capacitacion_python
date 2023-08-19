""" Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
para que también funcione cuando el día o el mes se introduzcan con un solo carácter. """
def obtener_fecha_valida():
    while True:
        fecha = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
        partes_fecha = fecha.split("/")
        if len(partes_fecha) == 3 and all(part.isdigit() for part in partes_fecha):
            dia, mes, anio = map(int, partes_fecha)
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= anio <= 2023:
                return dia, mes, anio
        print("Fecha inválida. Intente nuevamente.")

def mostrar_fecha(dia, mes, anio):
    print(f"Día: {dia} - Mes: {mes} - Año: {anio}")

dia, mes, anio = obtener_fecha_valida()

mostrar_fecha(dia, mes, anio)
