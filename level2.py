# obejectif puissance 4


def ajout(matrix, nb_col, c):

    i = 0
    while i < Nligne - 1 and matrix[i + 1][nb_col] == 0:
        i += 1

    matrix[i][nb_col] = c

    return i


def condition(matrix, vecteur, forme, coup):
    ###----####
    for i in range(len(vecteur)):
        k, l = vecteur[i]
        if not (matrix[k][l] in forme):
            continue
        condi = True
        j = i + 1
        cpt = 0
        while (
            j < len(vecteur) and cpt < coup - 1
        ):  # for j in range(i+1,i+coup) i + 1 < i + coup | j <coup
            kk, ll = vecteur[j]
            if not (matrix[k][l] == matrix[kk][ll]):
                condi = False
                break
            cpt += 1
            j = j + 1
        if condi and cpt == (coup - 1):
            return True

    return False


def deplacement(boat, direction, pos, coup):
    liste = []
    D = boat[direction]
    x, y = pos  # position suivante
    x += D[0]
    y += D[1]
    for c in range(coup - 1):
        if 0 <= x < Nligne and 0 <= y < Ncolonne:
            liste.append((x, y))
        x += D[0]
        y += D[1]
    return liste


def solver(matrix, pos, coup, liste_tuple):

    # ligne,colonne,diag 1 GH + DB, diag2 GB + DH

    for (avant, apres) in liste_tuple:
        liste = deplacement(boat, avant, pos, coup)
        liste.reverse()
        liste.append(pos)
        liste.extend(deplacement(boat, apres, pos, coup))
        if condition(matrix, liste, forme, coup):
            return True

    return False


def affichage(matrix):
    l = [str(i) for i in range(1, Ncolonne + 1)]
    print("|" + "|".join(l) + "|")
    for i in range(Nligne):
        ligne = matrix[i]
        l.clear()
        for j in ligne:
            if j == 0:
                car = " "
            else:
                car = j
            l.append(car)

        print(f"|" + "|".join(l) + "|")


def conversion(chaine):
    if not (chaine[0].isdigit()):
        print("error 1")
        exit()

    y = int(chaine[0])
    if not (1 <= y <= 7):
        print("error 2")
        exit()

    return y - 1


# main
Nligne = 6
Ncolonne = 7
matrix = [[0 for j in range(Ncolonne)] for i in range(Nligne)]
i = 0
joueur = ("joueur1", "joueur2")
forme = ("r", "j")
boat = {
    "haut": (0, -1),
    "bas": (0, 1),
    "droite": (1, 0),
    "gauche": (-1, 0),
    "diagDB": (1, 1),
    "diagGH": (-1, -1),
    "diagGB": (-1, 1),
    "diagDH": (1, -1),
}
liste_tuple = [
    ("gauche", "droite"),
    ("bas", "haut"),
    ("diagGH", "diagDB"),
    ("diagGB", "diagDH"),
]


i = 0
cpt = 0
coup = 4
lim = Nligne * Ncolonne
pos = (0, 0)

print(
    f"C'est une grille de taille {Nligne} X {Ncolonne}, les colonnes sont numérotés de 1 jusqu'à {Nligne}\n par exemple un choix de réponse 1 \n"
)

while not (solver(matrix, pos, coup, liste_tuple)) and cpt < lim:
    j = joueur[i]
    c = forme[i]
    rep = input(f"Choisir une colonne {j} : ")
    nb_col = conversion(rep)
    nb_lig = ajout(matrix, nb_col, c)
    pos = (nb_lig, nb_col)
    affichage(matrix)
    i = 1 - i # i = (i+1)%2
    cpt += 1

if cpt < lim:
    print(f"Le gagnant est {joueur[1-i]}")
else:
    print(f"match nulle")
