"""
Escribir un programa que almacene las asignaturas de un curso en una lista: Matemáticas,
Física, Química, Historia y Lengua, y pregunte al usuario la nota que ha sacado en cada
asignatura. Finalizado el pedido de las notas debe eliminar de la lista las asignaturas
aprobadas (iguales o mayores a 6). Y al final el programa debe mostrar por pantalla las
asignaturas que debe rendir en diciembre y en marzo, las que debe rendir en diciembre
son las que alcanzaron al menos un 4 y las que se rinden en marzo las que no llegaron.
"""
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Crear un diccionario para almacenar las notas de cada asignatura
notas = {}

# Solicitar las notas al usuario
for asignatura in asignaturas:
    try:
        nota = float(input(f"Ingrese la nota de {asignatura}: "))
        notas[asignatura] = nota
    except ValueError:
        print("Por favor, ingrese una nota válida.")

# Eliminar las asignaturas aprobadas (notas iguales o mayores a 6)
asignaturas_pendientes = [asignatura for asignatura, nota in notas.items() if nota < 6]

# Mostrar las asignaturas a rendir en diciembre (notas de al menos 4)
asignaturas_diciembre = [asignatura for asignatura, nota in notas.items() if nota >= 4]
print("Asignaturas a rendir en diciembre:")
for asignatura in asignaturas_diciembre:
    print(asignatura)

# Mostrar las asignaturas a rendir en marzo (notas menores a 4)
asignaturas_marzo = [asignatura for asignatura in asignaturas if asignatura not in asignaturas_diciembre]
print("Asignaturas a rendir en marzo:")
for asignatura in asignaturas_marzo:
    print(asignatura)
