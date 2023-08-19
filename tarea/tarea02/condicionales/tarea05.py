def determinar_grupo(nombre, sexo):
    nombre = nombre.upper()
    sexo = sexo.upper()

    if (sexo == "F" and nombre < "H") or (sexo == "M" and nombre > "M"):
        return "A"
    else:
        return "B"

nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (F para femenino, M para masculino): ")

grupo = determinar_grupo(nombre, sexo)

if grupo == "A":
    print("Usted pertenece al grupo A.")
elif grupo == "B":
    print("Usted pertenece al grupo B.")
else:
    print("Error: Ingrese un sexo válido (F o M).")
