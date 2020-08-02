from kanren import Relation, fact, facts, var, run, conde

Progenitor = Relation()
Hombre = Relation()
Mujer = Relation()

print("Bienvenido a tu arbol genealogico")

# Miembros de la familia
option = 9
names = []
while True:
    name = input("Nombre del miembro de la familia? ")
    print("Elige alguna de las opciones para empezar a crearlo")
    sex = input("1. A es hombre\n2. A es mujer\n")
    if sex == 1:
        fact(Hombre, name)
    else:
        fact(Mujer, name)
    names.append(name)
    option = int(input("Hay mas miembros? Ingresa 0 si ya no hay o cualquier otra tecla si aun hay mas"))

    if option == 0:
        break


option = 9

while True:
    print("Ahora vamos a crear las relaciones de progenitor")
    i = 0
    for n in names:
        print(f"{i}: {n}\n")
        i = i + 1

    name1 = int(input("Digite el numero del primer miembro familiar: "))
    print(f"Selecciono a {names[name1]}")
    name2 = int(input("Digite el numero del segundo miembro familiar: "))
    print(f"Selecciono a {names[name2]}")

    facts(Progenitor, (names[name1], names[name2]))
    print(f"La relacion creada fue {names[name1]} es progenitor de {names[name2]}")

    option = int(input("Hay mas relaciones? Ingresa 0 si ya no hay o cualquier otra tecla si aun hay mas"))

    if option == 0:
        break
