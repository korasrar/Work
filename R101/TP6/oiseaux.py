# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 2), ("Moineau", 5), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    # Parcours element ---------------------------
    """oiseau_max = 0
    oiseau_res = ''
    for observation in liste_observations:
        if observation[1] > oiseau_max:
            oiseau_max = observation[1]
            oiseau_res = observation[0]
    if oiseau_max == 0 :
        return None
    return oiseau_res"""
    # Parcours indices ---------------------------
    oiseau_max = 0
    oiseau_res = 0
    for i in range(len(liste_observations)):
        if liste_observations[i][1] > oiseau_max:
            oiseau_max = liste_observations[i][1]
            oiseau_res = i
    if oiseau_max == 0 :
        return None
    return liste_observations[oiseau_res][0]

def recherche_oiseau(nom,listefamille):
    for i in range(len(listefamille)):
        if nom in listefamille[i] :
            return listefamille[i]
    return None

def recherche_par_famille(famille,listefamille):
    listeoiseaux = []
    for i in range(len(listefamille)) :
        if famille in listefamille[i] :
            listeoiseaux.append(listefamille[i][0])
    if listeoiseaux == []:
        return None
    return listeoiseaux

def est_liste_observations(liste_observations):
    for i in range(1,len(liste_observations)):
        if liste_observations[i-1][0] < liste_observations[i][0] and liste_observations[i-1][1] != 0 :
            res = True
        else:
            return False
    return res
print(est_liste_observations(observations1))

def max_observations(liste_observations):
    maxobserv = 0
    for i in range(len(liste_observations)):
        if liste_observations[i][1] > maxobserv :
            maxobserv = liste_observations[i][1]
    return maxobserv

def moyenne_oiseaux_observes(liste_observations):
    somme = 0
    cpt = 0
    for i in range(len(liste_observations)):
        somme += liste_observations[i][1]
        cpt += 1
    return somme/cpt

def total_famille(liste_observations,listefamille):
    res = []
    ind1 = 0
    ind2 = 0
    while ind1 < liste_observations and ind2 < listefamille:
        listefamille[ind2][1]
        
#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)
