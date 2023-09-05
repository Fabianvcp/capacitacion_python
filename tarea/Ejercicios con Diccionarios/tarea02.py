""" 
Escriba un programa que tenga inicialmente un diccionario con los siguientes datos de
dos personas:
Nombre
Apellido
Edad
Email
Persona 1: Emilia, Cabrera de 23 años de edad, email ecabrera@curso.com
Persona 2: Gustavo Andrés, Peralta de 26 años de edad, email gperalta@curso.com
El programa debe permitir la carga de una persona más y agregarla al diccionario.
Ingresados los datos de esta persona nueva deben imprimirse los datos de las 3 personas
cargadas de manera tabular.
"""

# Diccionario inicial con datos de dos personas
personas = {
    1: {
        'Nombre': 'Emilia',
        'Apellido': 'Cabrera',
        'Edad': 23,
        'Email': 'ecabrera@curso.com'
    },
    2: {
        'Nombre': 'Gustavo Andrés',
        'Apellido': 'Peralta',
        'Edad': 26,
        'Email': 'gperalta@curso.com'
    }
}

# Solicitar los datos de una persona nueva
nombre_nuevo = input("Ingrese el nombre de la nueva persona: ")
apellido_nuevo = input("Ingrese el apellido de la nueva persona: ")
edad_nueva = int(input("Ingrese la edad de la nueva persona: "))
email_nuevo = input("Ingrese el email de la nueva persona: ")

# Obtener el número de la próxima persona
numero_persona_nueva = len(personas) + 1

# Agregar la nueva persona al diccionario
personas[numero_persona_nueva] = {
    'Nombre': nombre_nuevo,
    'Apellido': apellido_nuevo,
    'Edad': edad_nueva,
    'Email': email_nuevo
}

# Imprimir los datos de todas las personas de manera tabular
print("\nDatos de las personas:")
print("{:<5} {:<15} {:<15} {:<5} {:<20}".format("ID", "Nombre", "Apellido", "Edad", "Email"))
for id_persona, datos_persona in personas.items():
    print("{:<5} {:<15} {:<15} {:<5} {:<20}".format(id_persona, datos_persona['Nombre'], datos_persona['Apellido'], datos_persona['Edad'], datos_persona['Email']))
