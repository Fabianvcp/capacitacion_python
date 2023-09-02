"""
Dada una cadena de texto que representa una fecha (mes/día/año truncado): ‘3/30/20’

transfórmela en otra cadena de texto con el siguiente formato: ‘31-12-2020’ (día-mes-
año completo)
"""
from datetime import datetime

# Cadena de fecha en formato 'mes/día/año truncado'
cadena_fecha = '3/30/20'

# Convertir la cadena en un objeto datetime
fecha_objeto = datetime.strptime(cadena_fecha, '%m/%d/%y')

# Formatear la fecha en el nuevo formato 'día-mes-año completo'
nueva_cadena_fecha = fecha_objeto.strftime('%d-%m-%Y')

print(nueva_cadena_fecha)
