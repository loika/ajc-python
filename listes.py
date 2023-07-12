# Décrivez une fonction "strtolist" prenant une chaîne de caractère en paramêtre
# et qui renvoie une liste contenant les lettres majuscules de la chaîne (sans doublons)
# Ex: "CouCOu" => ["C","O"]

# Décrivez une fonction "listotstr" qui prend une liste de mots en paramêtre
# et qui renvoie une chaîne de caractère avec les mots séparés par un espace
# Ex: ["bonjour","à","tous"] => "bonjour à tous"

# Décrivez une fonction "halfstring" qui prend une chaîne de caractère en paramêtre
# et qui renvoie une liste contenant une lettre sur deux de la chaîne
# Ex: "good morning" => ['o','d','o','n','n']

# Décrivez une fonction "completenumber" qui prend une liste de nombres en paramêtre
# et qui renvoie une liste contenant les chiffres qui manque dans la liste
# Ex: [1,4,5,6,8,9] => [1,2,3,4,5,6,7,8,9]

# Décrivez une fonction "fullequals" qui prend 2 listes en paramêtre
# et qui renvoie True/False si les deux listes contiennent les même valeurs peut importe l'ordre

# Decrivez une fonction displaygrid qui affiche une grille (colonne avec des nombres et lignes avec des lettres) à partir d'un tableau (contenant 0 ou 1) passé en paramêtre
# Quand la valeur d'un élément est 1 la case doit afficher un '-' sinon un espace
# Ex: [[0,0,0,1,0,1]] =>
#   " |1|2|3|4|5|6|"
#   "A| | | |-| |-|"

import sys  # ne vous ocuppez pas de ça
import io  # ne vous ocuppez pas de ça


# Vos fonctions ici:
def strtolist(chaine):


# Ne rien toucher à partir de là
print('-- strtolist --')
print(strtolist('HelLo WOrLd') == ['H', 'L', 'W', 'O'])
print(strtolist('PyThON C\'eST syMpaThIqUE') == [
      'P', 'T', 'O', 'N', 'C', 'S', 'M', 'I', 'U', 'E'])
print(strtolist('3Eme-TeSt') == ['E', 'T', 'S'])


# print('-- listotstr --')
# print(listotstr(['bonjour','à','tous'])=='bonjour à tous')
# print(listotstr(['J\'ai','10','ans'])=='J\'ai 10 ans')

# print('-- halfstring --')
# print(halfstring("good morning")==['o','d','o','n','n'])
# print(halfstring("c'est la fête le 22 juillet")==['e','t','a','ê','e','e','u','l','e'])

# print('-- completenumber --')
# print(completenumber([1,3,4,5,7])==[1,2,3,4,5,6,7])
# print(completenumber([0,4])==[0,1,2,3,4])
# print(completenumber([-1,0,2,4,5,9])==[-1,0,1,2,3,4,5,6,7,8,9])
# print(completenumber([])==[])

# print('-- fullequals --')
# print(fullequals([1,4,6,2],[4,6,1,2])==True)
# print(fullequals([1,3,5,6],[3,5,4,1,7])==False)
# print(fullequals([1,4,6,2,2],[4,6,1,2])==False)
# print(fullequals([1,4,6,2,4],[4,6,1,6,2])==False)

# old_stdout = sys.stdout # Memorize the default stdout stream
# sys.stdout = buffer = io.StringIO()

# grid1line = [[0,0,0,1,0,1]]
# grid2 = [
#     [1,1,0,0,0,1,0,0],
#     [0,0,0,1,0,1,0,0],
#     [0,1,0,1,0,1,0,0],
#     [0,1,0,1,0,0,0,0],
#     [0,1,0,0,1,1,1,1],
#     [0,1,0,0,0,0,0,0]
# ]
# displaygrid(grid1line)
# displaygrid(grid2)


# sys.stdout = old_stdout # Put the old stream back in place
# whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
# print(whatWasPrinted)
