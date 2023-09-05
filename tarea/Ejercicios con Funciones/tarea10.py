"""
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
[{'año': 2000, '
metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True,
'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje':
False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True,
'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje':
False, 'zona': 'A'}]
Construir una función que permita hacer búsqueda de inmuebles en función de un
presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y
devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los
inmuebles de la lista que se devuelva deben incorporar un nuevo par, clave/valor, a cada
diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las
siguiente fórmula en función de la zona:
Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-
antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-
antiguedad/100) * 1.5
"""
def calcular_precio(inmueble):
    precio = ''
    if inmueble['zona'] == 'A':
        precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - (2023 - inmueble['año']) / 100)
    elif inmueble['zona'] == 'B':
        precio = (inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + inmueble['garaje'] * 15000) * (1 - (2023 - inmueble['año']) / 100) * 1.5
    return precio

def buscar_inmuebles_por_presupuesto(lista_inmuebles, presupuesto):
    inmuebles_cumplen_presupuesto = []

    for inmueble in lista_inmuebles:
        precio_inmueble = calcular_precio(inmueble)
        if precio_inmueble <= presupuesto:
            inmueble['precio'] = precio_inmueble
            inmuebles_cumplen_presupuesto.append(inmueble)

    return inmuebles_cumplen_presupuesto

# Ejemplo de uso:
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presupuesto = 100000  # Define aquí tu presupuesto máximo
inmuebles_disponibles = buscar_inmuebles_por_presupuesto(inmuebles, presupuesto)

for inmueble in inmuebles_disponibles:
    print(f'Precio: ${inmueble["precio"]:.2f}, Año: {inmueble["año"]}, Metros: {inmueble["metros"]}m², Habitaciones: {inmueble["habitaciones"]}, Garaje: {inmueble["garaje"]}, Zona: {inmueble["zona"]}')
