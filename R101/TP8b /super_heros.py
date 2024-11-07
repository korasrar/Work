malistehihi = {
    'Spriderman': (5, 5, 'araignée a quattre pattes'),
    'Hulk': (7, 4, 'grand homme vert'),
    'Rei Ayanami': (3, 8, 'première enfant'),
    'Shinji Ikari': (5, 7, 'second enfant'),
    'Fluttershy': (3, 5, 'bleeeh')
}

def intelligence_moyenne(personnages):
    """Calcul la moyenne des intelligences des personnages

    Args:
        personnages (dico): Liste de personnages avec leur force intelligence et desc

    Returns:
        float: moyenne intelligence
    """    
    somme = 0
    cpt = 0
    for info in personnages.values():
        somme += info[1]
        cpt += 1
    if cpt > 0 :
        return somme/cpt
    return None

def kikelplusfort(personnages):
    """Renvoie le nom du perso le plus fort

    Args:
        personnages (dico): Liste de personnages avec leur force intelligence et desc

    Returns:
        str: Nom du perso le plus fort
    """    
    valforce = 0
    nomperso = ""
    for perso,info in personnages.items():
        if valforce < info[0]:
            valforce = info[0]
            nomperso = perso
    return nomperso

def combienDeCretins(personnages):
    """Renvoie le nombre de p ersonnages dont l'intelligence est strictement inférieure à la moyenne

    Args:
        personnages (dico): Liste de personnages avec leur force intelligence et desc

    Returns:
        int: Nombre de perso qui a un int en dessous de la moyenne
    """    
    cpt = 0
    moyenneint = intelligence_moyenne(personnages)
    for info in personnages.values():
        if moyenneint > info[1]:
            cpt += 1
    return cpt

