# Décrivez une fonction printline qui prend une liste de tuple (nom=string,prenom=string,age=int) en paramêtre
# et qui affiche la description des tuples
# Ex [('Doe','John',54)] => 'La personne s'appelle John Doe et elle a 54 ans'

# Décrivez une fonction addinfo qui prend une liste de tuple (nom=string,prenom=string,age=int) en paramêtre
# et qui renvoie une liste des tuples modifiés. Il faut ajouter un identifiant (première lettre prénom + nom) et son année de naissance 

# Décrivez une fonction coordtogrid qui prend 2 nombres (width,height) en paramêtre et une liste de coordonnées (x,y) en paramêtre et qui renvoie un tableau
# En reprenant la fonction dans l'exercices des listes qui affihce une grille, on veut cette fois créer le tableau passé en paramêtre de cette fonction
# le nombre de listes dans le tableau est donné par la valeur de "height"
# le nombre d'élément par liste est donnée par la valeur de "width"
# les éléments des listes sont des nombres, 0 par défaut
# les tuples passés en paramêtre définisse les indexs auquels un élément du tableau doit avoir la valeur 1
# Ex: 3,4, [(2,3),(0,2)] => 
# [[0,0,0], => y=0
#  [0,0,0], => y=1
#  [1,0,0], => y=2
#  [0,0,1] => y=3
# ] 
# Vous pouvez vous aider de la fonction displaygrid pour afficher ce que vous renvoyez

import sys # ne vous ocuppez pas de ça
import io # ne vous ocuppez pas de ça
import datetime # ne vous ocuppez pas de ça

# Vos fonctions ici:









def displaygrid(grid):

    def linetostr(line): # pour afficher une ligne 
        linestr = '|'
        for i in line:
            if i==1: linestr+='-'
            else: linestr+=' '
            linestr+='|'
        return linestr+'\n'

    # construction de la première ligne = " |1|2|3|4|5|6|"
    gridstr = ' |'
    if len(grid)==0:
        return
    for i in range(1,len(grid[0])+1):
        gridstr+=str(i)+'|'
    gridstr+='\n'

    # construction des lignes
    char = 65 # lettre 'A'
    for line in grid:
        gridstr+=chr(char)+linetostr(line)
        char+=1
    print(gridstr)




# Ne rien toucher à partir de là
# ---------------------------------------
print('-- printline --')
old_stdout = sys.stdout # Memorize the default stdout stream
sys.stdout = buffer = io.StringIO()

printline([('Doe','John',54)])
printline([('Doe','John',54),('Dupont','Jean',45),('LeGrand','Hélène',36)])

sys.stdout = old_stdout # Put the old stream back in place
whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
print(whatWasPrinted)


print(whatWasPrinted=='La personne s\'appelle John Doe et elle a 54 ans.\nLa personne s\'appelle John Doe et elle a 54 ans.\nLa personne s\'appelle Jean Dupont et elle a 45 ans.\nLa personne s\'appelle Hélène LeGrand et elle a 36 ans.\n')

print('-- addInfo --')
addinfo([('Doe','John',54),('Dupont','Jean',45),('LeGrand','Hélène',36)])

print(addinfo([('Doe','John',54)])==[('Doe','John',54,'JDoe',1968)])
print(addinfo([('Doe','John',54),('Dupont','Jean',45)])==[('Doe','John',54,'JDoe',1968),('Dupont','Jean',45,'JDupont',1977)])

# un exemple de liste de coordonées pour que vous testiez: coords = [(0,0),(1,0),(4,0),(4,1),(4,2)]
# Avec display grid doit afficher:
#  |1|2|3|4|5|
# A|-|-| | |-|
# B| | | | |-|
# C| | | | |-|
# D| | | | | |
# E| | | | | |

displaygrid(coordtogrid(9,9,[(0,0),(1,0),(4,0),(4,1),(4,2)]));
