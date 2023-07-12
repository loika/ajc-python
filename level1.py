# objectif le tic tac toc

# def


def condition(vecteur):
    # pour les lignes ou les colonnes
    if (
        vecteur[0] in forme
        and vecteur[0] == vecteur[1]
        and vecteur[1] == vecteur[2]
        and vecteur[1] == vecteur[2]
    ):
        return True
    return False


def solver(matrix, forme):

    for i in range(3):
        ligne = matrix[i]
        colonne = [matrix[0][i], matrix[1][i], matrix[2][i]]
        if condition(ligne) or condition(colonne):
            return True

    # diag
    diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diag2 = [matrix[0][2], matrix[1][1], matrix[2][0]]

    if condition(diag1) or condition(diag2):
        return True

    return False


def affiche(matrix, alpha):

    print(" |" + "|".join(["1", "2", "3"]) + "|")
    for i in range(3):
        ligne = matrix[i]
        l = []
        for j in ligne:
            if j == 0:
                car = " "
            else:
                car = j
            l.append(car)

        print(f"{alpha[i]}|" + "|".join(l) + "|")

    return None


def conversion(chaine):
    if not (chaine[0].isalpha()) or not (chaine[1].isdigit()):
        print("error 1")
        exit()

    if chaine[0] == "A":
        x = 0
    elif chaine[0] == "B":
        x = 1
    elif chaine[0] == "C":
        x = 2
    else:
        print("error 2")

    if not (chaine[1].isdigit()):
        exit()

    y = int(chaine[1])
    if not (1 <= y <= 3):
        print("error 3")
        exit()

    return (x, y - 1)


# main

matrix = [[0 for j in range(3)] for i in range(3)]
i = 0
joueur = ("joueur1", "joueur2")
forme = ("x", "-")
alpha = ["A", "B", "C"]
print(
    "pour le choix de la case A,B,C désigne les ligne et 1,2,3 colonne par exemple A1 déisgne la casse tout en haut à gauche\n"
)


i = 0
cpt = 0
while not (solver(matrix, forme)) and cpt < 9:
    j = joueur[i]

    rep = input(f"au tour du {j} de donner une réponse ")
    x, y = conversion(rep)
    matrix[x][y] = forme[i]
    affiche(matrix, alpha)

    i = 1 - i
    cpt += 1

if not (cpt == 9):
    print(f"Le gagnant est {joueur[1-i]}")
else:
    print("match nulle")
