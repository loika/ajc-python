# Décrivez une fonctions printinfo qui prend un dictionnaire en paramêtre et affiche les informations d'une personne contenu dedans
# Le dictionnaire est construit de la manère suivante: {'nom':string,'prenom':string,age:int}

# Décrivez une fonction boatstocoords qui prend une liste de dictionnaire en paramêtre et renvoie une liste de tuples
# Les objets sont construits comme ceci: {x:int,y:int,direction:string,length:int}
# Ils représentent des lignes commencant a (x,y) de longueur length et orienté par direction ('haut','bas','gauche' ou 'droite')
# Attention l'origine de la grille est en haut à gauche
# Vous devez renvoyez une liste de tuples correspondant au coordonées traversées par ces lignes (0,0) est en bas à gauche
# Ex: [{'x':3,'y':5,'direction':'bas','length':4}] => [(3,5),(3,6),(3,7),(3,8)]

# Vos fonctions ici:


def printinfo(dico):
    for key, value in dico.items():
        print(key, ":", value)
    return None


def boatstocoords(liste_dico):

    liste = []

    for dico in liste_dico:
        x = dico["x"]
        y = dico["y"]
        taille = dico["length"]
        d = dico["direction"]
        if d == "bas":
            D = [0, 1]
        elif d == "haut":
            D = [0, -1]
        elif d == "droite":
            D = [1, 0]
        else:
            D = [-1, 0]

        for i in range(taille):
            liste.append((x, y))
            x += D[0]
            y += D[1]

    return liste


def coordtogrid(width, height, coords):
    # creation de la grille
    grid = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            line.append(0)
        grid.append(line)

    # affectation des valeurs dans la grille en fonction des coordonées
    for coord in coords:
        grid[coord[1]][coord[0]] = 1

    return grid


def displaygrid(grid):
    def linetostr(line):  # pour afficher une ligne
        linestr = "|"
        for i in line:
            if i == 1:
                linestr += "-"
            else:
                linestr += " "
            linestr += "|"
        return linestr + "\n"

    # construction de la première ligne = " |1|2|3|4|5|6|"
    gridstr = " |"
    if len(grid) == 0:
        return
    for i in range(1, len(grid[0]) + 1):
        gridstr += str(i) + "|"
    gridstr += "\n"

    # construction des lignes
    char = 65  # lettre 'A'
    for line in grid:
        gridstr += chr(char) + linetostr(line)
        char += 1
    print(gridstr)


# Ne rien toucher à partir de là
# ---------------------------------------
# Pour tester printinfo:
printinfo({"nom": "Dupont", "prenom": "Jean", "age": 15})


# Ne rien toucher à partir de là
# ---------------------------------------
# Pour tester printinfo:
printinfo({"nom": "Dupont", "prenom": "Jean", "age": 15})


coords = boatstocoords([{"x": 3, "y": 5, "direction": "bas", "length": 4}])
print(coords == [(3, 5), (3, 6), (3, 7), (3, 8)])


coords = boatstocoords(
    [
        {"x": 3, "y": 5, "direction": "bas", "length": 4},
        {"x": 0, "y": 0, "direction": "bas", "length": 2},
        {"x": 6, "y": 2, "direction": "gauche", "length": 2},
        {"x": 0, "y": 5, "direction": "droite", "length": 4},
    ]
)
print(
    coords
    == [
        (3, 5),
        (3, 6),
        (3, 7),
        (3, 8),
        (0, 0),
        (0, 1),
        (6, 2),
        (5, 2),
        (0, 5),
        (1, 5),
        (2, 5),
        (3, 5),
    ]
)


# grid = coordtogrid(10,10,coords)
# displaygrid(grid)

# coords = boatstocoords([{'x':3,'y':5,'direction':'nimportequoi','length':4}])
