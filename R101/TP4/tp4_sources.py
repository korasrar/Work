# --------------------------------------
# EXERCICE N°1
# --------------------------------------

def plus_long_plateau(chaine):
    """recherche la longueur du plus grand plateau d'une chaine
    Args:
        chaine (str): une chaine de caractères

    Returns:
        int: la longueur de la plus grande suite de lettres consécutives égales
    """
    lg_max = 0  # longueur du plus grand plateau déjà trouvé
    lg_actuelle = 0  # longueur du plateau actuel
    for i in range(len(chaine)):
        if chaine[i] == chaine[i-1]:  # si la lettre actuelle est égale à la précédente
            lg_actuelle += 1
        else : 
            if lg_actuelle > lg_max:  # si la lettre actuelle est différente de la précédente
                lg_max = lg_actuelle
            lg_actuelle = 1
    if lg_actuelle > lg_max:  # cas du dernier plateau
        lg_max = lg_actuelle
    return lg_max
print(plus_long_plateau("aaaBbbggkjjsqqqq"))

# --------------------------------------
# EXERCICE N°2
# --------------------------------------

def ville_peuple(liste_villes,population):
    populas = 0
    villeplus = ""
    for i in range(1,len(liste_villes)):
        if population[i] > populas :
            populas = population[i]
            villeplus = liste_villes[i]
    return villeplus
print(ville_peuple(["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux", "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"],[45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463, 25725]))
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux", "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463, 25725]

# --------------------------------------
# EXERCICE N°3
# -------------------------------------- 

def newint(nombrestr):
    nombre = 0
    chiffres = "0123456789"
    for i in range(len(nombrestr)):
        for c in range(len(chiffres)):
            if nombrestr[i] == chiffres[c] :
                nombre = c+nombre*10
    return nombre
print(newint("2021"))

# --------------------------------------
# EXERCICE N°5
# -------------------------------------- 
def wordinlist(phrase):
    listee = []
    addword = ""
    for i in range(len(phrase)):
        if phrase[i].isalpha():
            addword = addword + phrase[i]
        if not phrase[i].isalpha() and addword != '':
            listee.append(addword)
            addword = ""
    return listee
print(wordinlist("Cela fait déjà 28 jours! 28 jours à l'IUT'O! Cool!!"))