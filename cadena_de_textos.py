cadena_mas_1_linea = ''' 
    Aca pueden escribir
    "n" cadenas de texto
    larga
'''
"""
    Consejo: El modificador r es muy utilizado para la escritura de expresiones regulares
"""

conversion = str(9)

secuencia_de_escape = 'Hola \n¿Todo bien?'

msg1 = 'Hola'
msg2 = '¿todo bien?'

print(msg1,msg2,sep='\n',end="!")

concatenacion= msg1 + ', ' + msg2

repetir_cadena = msg1 * 4

msg3 = 'Hola, mundo'
obtener_un_caracter= msg3

print(obtener_un_caracter[]) 
"""
-10-9-8-7-6-5-4-3-2-1
H O L A ,   M U N D O
0 1 2 3 4 5 6 7 8 9 10

Es posible extraer «trozos» («rebanadas») de una cadena de texto2. Tenemos varias
aproximaciones para ello:
[:] Extrae la secuencia entera desde el comienzo hasta el final. Es una especia de copia de
toda la cadena de texto.
[start:] Extrae desde start hasta el final de la cadena.
[:end] Extrae desde el comienzo de la cadena hasta end menos 1.
[start:end] Extrae desde start hasta end menos 1.
[start:end:step] Extrae desde start hasta end menos 1 haciendo saltos de tamaño step.

"""

longitud = len(msg1)


'encontrar una palabra'
proverb = 'Más vale malo conocido que bueno por conocer'
'malo' in proverb
'bueno' in proverb
'regular' in proverb

"""
    Habría que prestar atención al caso en el que intentamos descubrir si una subcadena no está
    en la cadena de texto
"""

dna_sequence = 'ATGAAATTGAAATGGGA'
not( 'C 'in dna_sequence) # Primera aproximación
'C' not in dna_sequence # Forma pionic

dividir_cadena= msg3.split(",")

#!limpieza por la izquierda es lstrip y por la derecha desde el fin es rstrip, limpiar caracter especifico es con strip('caracter')
limpiar_cadenas = msg3.strip()
#! Buscar elementos
lyrics = '''Quizás porque mi niñez
... Sigue jugando en tu playa
... Y escondido tras las cañas
... Duerme mi primer amor
... Llevo tu luz y tu olor
... Por dondequiera que vaya'''

lyrics.startswith('Quizás')

lyrics.endswith('Final')
#Entoces la primera ocurrencia de alguna subcadena
lyrics.find('amor')

lyrics.index('amor')
"""
Tanto find() como index() devuelven el indice de la primera ocurrencia de la subcadena que estamos
buscando, pero se diferencia en su comportamiento cuando la subcadena buscando no existe
en find devolvera un -1 y en index devolvera traceback(most recent call last)
"""

#Contabilizar el número de veces que aparece una subcadena
lyrics.count('mi')

#! Remplazar elementos ---------------------


proverb2 = ' Quien Mal anda Mal acaba'

proverb2.replace('mal', 'bien')

proverb2.replace('Mal', 'Bien', 1) #solo remplaza uno


#!Mayusculas y minúsculas -----------------------

proverb = 'Quien a buen árbol se arrima Buena Sombra le cobija'

proverb.capitalize() #Inicia con mayuscula

proverb.title() #Todas Las Palabras Estan En Mayusculas

proverb.upper() #TODA LA CADENA ESTA EN MAYUSCULA

proverb.lower() #toda la cadena esta en minuscula 

#!Identificación de caracteres ------------------

""" 
    Hay veces que recibimos información textual de distintas fuentes
    de las que necesitamos identificar qué tipo de caracteres contienen
"""
#Detectar si todos los cartacteres son letras o números
'R2D2'.isalnum()

'C3-PO'.isalnum()

#detectar si es todolos caracteres son números
'314'.isnumeric()

'3.14'.isnumeric()

#dectectar si todos los caracteres son letras
'abc'.isalpha()

'a-b-c'.isalpha()

#detectar si son mayusculas o minusculas

'BIG'.isupper()

'small'.islower()

'First Heading'.istitle()

#Formateando cadenas

mount_height = 3718

print(f'{mount_height:10d}')  #      3718

print(f'{mount_height:010d}')# 0000003718

#dando formato en otras bases:
value = 0b10010011

print(f'{value}')

print(f'{value:b}')

value = 0o47622
print(f'{value}')

print(f'{value:o}')

value = 0xab217
print(f'{value}')

print(f'{value:x}')

pi = 3.14159265

f'{pi:f}' #6 decimales por defectos

f'{pi:.3f}' # decimales

"""
    >>>f {pi:12f}
    3.141593
    >>> f {pi:7.2f}
    3.14
    >>> f {pi:07.2f}
    0003.14
    >>> f {pi:.010f}
    3.1415926500
    >>> f {pi:e}
    3.141593e+00
"""

text1 = 'how'
text2 = 'are'
text3 = 'you'

f'{text1:<7s}|{text2:^11s}|{text3:>7s}'# how | are | you
f'{text1:-<7s}|{text2:·^11s}|{text3:->7s}'# how----|····are····|----yo

#! Modo <<debug>> -------

serie =  'The Simpsons'
imdb_rating = 8.7
num_seasons = 30

f'{serie=}'

f'{imdb_rating=}' #'imdb_rating=8.7'
f'{serie[4:]=}' # incluso podemos añadir expresiones! "serie[4:]= Simpsons "
f'{imdb_rating / num_seasons=}' # imdb_rating / num_seasons=0.29

#! Modo <<representacion>> -------

name = 'Steven Spielberg'

print(f'{name}')
print(f'{name!r}')

#! Caracteres unicode
#para ampliar los caracteres unicode https://unicode-table.com/en/blocks/
rocket_code = 0x1F680
rocket = chr(rocket_code)
print(rocket)
#la funcion ord() permite obter el código(decimal) de un carácter a partir de su representacion:

rocket_code = hex(ord(rocket))
rocket_code
'\N{Helicopter}'

#! Comparar cadenas
"""
Cuando comparamos dos cadenas de texto lo hacemos en términos lexicográficos. Es decir,
se van comparando los caracteres de ambas cadenas uno a uno y se va mirando cuál está
«antes».
"""
'arca' < 'arpa' #ar es igual para ambas

ord('c')

ord('p')