"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos
los ingredientes que lleva.
Ejemplo
Bienvenido a la pizzeria Bella Napoli.
Tipos de pizza
1- Vegetariana
2- No vegetariana
Ingredientes de pizzas no vegetarianas
1- Peperoni
2- Jamón
3- Salmón
Pizza no vegetarina con mozarrella, tomate y jamón
"""

def mostrar_menu():
    print("Bienvenido a la pizzeria Bella Napoli.")
    print("Tipos de pizza:")
    print("1- Vegetariana")
    print("2- No vegetariana")

def mostrar_menu_ingredientes_no_vegetarianos():
    print("Ingredientes de pizzas no vegetarianas:")
    print("1- Peperoni")
    print("2- Jamón")
    print("3- Salmón")

def mostrar_ingredientes_elegidos(es_vegetariana, ingrediente_elegido):
    tipo_pizza = "vegetariana" if es_vegetariana else "no vegetariana"
    print(f"Pizza {tipo_pizza} con mozzarella, tomate y {ingrediente_elegido}")

mostrar_menu()


opcion = input("Ingrese el número correspondiente al tipo de pizza que desea (1 o 2): ")

if opcion == "1":
    mostrar_menu_ingredientes_no_vegetarianos()
    ingrediente_elegido = input("Ingrese el número correspondiente al ingrediente que desea (1, 2 o 3): ")
    ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
    ingrediente_elegido = ingredientes_no_vegetarianos[int(ingrediente_elegido) - 1]
    mostrar_ingredientes_elegidos(True, ingrediente_elegido)
elif opcion == "2":
    print("Ingredientes disponibles para pizza vegetariana: 1- Pimiento, 2- Tofu")
    ingrediente_elegido = input("Ingrese el número correspondiente al ingrediente que desea (1 o 2): ")
    ingredientes_vegetarianos = ["Pimiento", "Tofu"]
    ingrediente_elegido = ingredientes_vegetarianos[int(ingrediente_elegido) - 1]
    mostrar_ingredientes_elegidos(False, ingrediente_elegido)
else:
    print("Opción no válida. Por favor, seleccione 1 o 2 para el tipo de pizza.")
