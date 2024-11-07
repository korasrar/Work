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

troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
troupeau_de_perrette = {'veau':14, 'vache':7, 'poule':42}
troupeau_vide = dict()  

def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    for animal,num in troupeau1.items():
        if animal in troupeau2 :
            troupeau2[animal] += num
        else:
            troupeau2[animal] = num
    return troupeau2
print(reunion_troupeaux(troupeau_de_perrette,troupeau_vide))
