""" Escriba un programa en Python que acepte los nombres y el apellido de una persona y los
imprima en orden inverso separados por una coma. Utilice f-strings para implementarlo.
o Entrada: name=Sergio Alejandro; surname= Quintero
o Salida: Quintero, Sergio Alejandro """
nombre_completo =  input('Ingrese su nombre completo sin apellido:\n')
apellido = input('Ingrese su apellido:\n')

print(f'{apellido},{nombre_completo}')