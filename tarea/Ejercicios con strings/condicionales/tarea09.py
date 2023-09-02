"""
Escriba un programa en Python que acepte la opción de dos jugadoras en Piedra-Papel-
Tijera e indique el resultado de la competencia

Ejemplo
• Persona 1 juega: piedra
• Persona 2 juega: papel
• Salida: Gana Persona 2: El papel envuelve a la piedr
"""

def juego_piedra_papel_tijera(jugador1, jugador2):
    opciones_validas = ["piedra", "papel", "tijera"]

    if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
        return "Opción inválida. Por favor, elija entre piedra, papel o tijera."

    if jugador1 == jugador2:
        return "Es un empate."

    if (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        return "Gana Persona 1."
    else:
        return "Gana Persona 2."

try:
    jugador1 = input("Persona 1 juega (piedra, papel o tijera): ").lower()
    jugador2 = input("Persona 2 juega (piedra, papel o tijera): ").lower()

    resultado = juego_piedra_papel_tijera(jugador1, jugador2)
    print(resultado)
except ValueError:
    print("Error: Ingrese una opción válida.")
