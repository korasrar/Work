"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
ecosysteme_3 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard' }

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] in ecosysteme:
        return False
    return True


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    animal_actuel = animal 
    ind = 0
    while ecosysteme[animal_actuel] in ecosysteme and ecosysteme[animal_actuel] is not None and len(ecosysteme) > ind:
        animal_actuel = ecosysteme[animal_actuel]
        ind += 1
    if len(ecosysteme) > ind and ecosysteme[animal_actuel] is not None:
        return True
    return False
print(en_voie_disparition(ecosysteme_1,'Loup'))

def animaux_en_danger(ecosysteme):
    """
    renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate
    """
    ...


def especes_en_voie_disparition(ecosysteme):
    """
    renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ...