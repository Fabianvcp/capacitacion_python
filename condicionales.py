
#! comentarios: reglas

"""
Reglas para escribir buenos comentarios:6
1. Los comentarios no deberían duplicar el código.
2. Los buenos comentarios no arreglan un código poco claro.
3. Si no puedes escribir un comentario claro, puede haber un problema en el código.
4. Los comentarios deberían evitar la confusión, no crearla.
5. Usa comentarios para explicar código no idiomático.
6. Proporciona enlaces a la fuente original del código copiado.
Aprende Python
7. Incluye enlaces a referencias externas que sean de ayuda.
8. Añade comentarios cuando arregles errores.
9. Usa comentarios para destacar implementaciones incompletas.
"""

#! ancho del Código
"""
    Así las líneas de más
    de 80 caracteres se siguen visualizando correctamente. Hay personas que son más estrictas
    en este límite y otras más flexibles.
    En caso de que queramos romper una línea de código demasiado larga, tenemos dos
    opciones:
    
    usar la barra invertida \ :
    factorial = 4*3*2*1
    factoria = 4 *\
            3 * \
            2 * \
            1       

    usar los paréntesis 
     factoria = (4 *
            3 * 
            2 * 
            1)       
"""

#! La setencia if
temperature = 40
if temperature > 35:
    print("Aviso por temperatura")
    
if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
elif temperature < 30:
    print('Nivel naranja')
else:
    print('Nivel rojo')
    
#Simplificación del código
fire_risk = 'LOW' if temperature < 30 else 'HIGH'

"""
        Operador        Símbolo
        Igualdad            ==
        Desigualdad         !=
        Menor que           <
        Menor o igual que   <=
        Mayor que           >
        Mayor o igual que   >=
        
        operadores logicos
        
        and
        or
        not

"""
#!circuito logico
power = 10
signal_4g = 60

power > 25 and signal_4g > 10

#Valor nulo
value = None


#!sentencias match-case


color = '#FF0000'

match color:
    case '#FF0000':
        print('#FF0000')
    case '#00FF00':
        print('#00FF00')
    case '#0000FF':
        print('#0000FF')
    case _: #en caso de no encontrar el valor buscado tendras esta opcion
        print('Unknown Color!')    
        

