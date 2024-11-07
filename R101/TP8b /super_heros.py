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
        personnages (dico): Liste le personneages avec leur force intelligence et desc

    Returns:
        float: moyenne intelligence
    """    
    somme = 0
    cpt = 0
    for intelligence in personnages.values():
        somme += intelligence[1]
        cpt += 1
    if cpt > 0 :
        return somme/cpt
    return None

