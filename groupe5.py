from random import randint

nb = randint(0,100)

nombre=int(input("Proposez un nombre :"))
iter = 1
while not(nb == nombre):
    if nb < nombre:
        print("-")
    elif nb == nombre:
        break
    else:
        print("+")
    nombre=int(input("Proposez un nombre :"))
    iter += 1

print(f"gagné en {iter} coup(s)")