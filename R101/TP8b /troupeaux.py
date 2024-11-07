# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    somme = 0
    for num in troupeau.values():
        somme += num
    return somme


def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    animaux = set()
    for animal in troupeau.keys():
        animaux.add(animal)
    return animaux

def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    for num in troupeau.values():
        if num > 30 :
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    maxnum = 0
    maxanimal = None
    for animal,num in troupeau.items():
        if num > maxnum :
            maxnum = num
            maxanimal = animal
    return maxanimal

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    listeanimaux = []
    for num in troupeau.values():
        if num < 5:
            return False
    return True


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    troupeaufinale = {}
    if len(troupeau1) != 0:
        for animal,num in troupeau1.items():
            troupeaufinale[animal] = num
    if len(troupeau2) != 0:
        for animal,num in troupeau2.items():
            if animal in troupeaufinale :
                troupeaufinale[animal] += num
            else:
                troupeaufinale[animal] = num
    return troupeaufinale
print(reunion_troupeaux({'veau':14, 'vache':7, 'poule':42} , {'vache':3,'ane':60,'poule':37,'cochon':1,'lombric':7}))

