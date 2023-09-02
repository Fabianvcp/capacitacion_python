""" Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @)
pero con dominio educ.ar """

email = input('ingrese su direccion de correo electronico:\n')
correo = email.split('@')

print(f'su correo nuevo es {correo[0]}@edu.ar')