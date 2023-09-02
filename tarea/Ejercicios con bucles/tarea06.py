"""
scriba un programa que muestre el movimiento de un caballo en un tablero de ajedrez,
suponiendo que su posición está formada por las coordenadas (x , y), siendo “x” la casilla
horizontal en la que se encuentra e “y” la casilla vertical, tomando como (1, 1) la casilla
inferior izquierdo del tablero. El programa simulará el movimiento de un «caballo» de
ajedrez moviéndose de forma alterna de la siguiente manera: primero avanzando 2
posiciones en x y 1 posición en y. En el siguiente movimiento se moverá 1 posición
en x más 2 posiciones en y. El programa deberá ir mostrando los puntos por los que va
pasando el «caballo» mientras no se salga del tablero.
Ejemplo
• Salida: (1, 1) (2, 3) (4, 4) (5, 6) (7, 7)

"""

# Tamaño del tablero de ajedrez (en número de casillas)
tamanio_tablero = 8

# Posición inicial del caballo (1, 1)
x, y = 1, 1

# Mostrar la posición inicial
print(f"({x}, {y})", end=" ")

# Definir los movimientos del caballo
movimientos = [(2, 1), (1, 2)]

# Realizar el movimiento del caballo mientras esté dentro del tablero
while True:
    # Intentar cada uno de los movimientos alternativos
    movimiento_valido = False
    for dx, dy in movimientos:
        nuevo_x, nuevo_y = x + dx, y + dy
        if 1 <= nuevo_x <= tamanio_tablero and 1 <= nuevo_y <= tamanio_tablero:
            x, y = nuevo_x, nuevo_y
            movimiento_valido = True
            print(f"({x}, {y})", end=" ")
            break
    
    # Si no se puede realizar ninguno de los movimientos, salir del bucle
    if not movimiento_valido:
        break

print()  # Imprimir una línea en blanco al final
