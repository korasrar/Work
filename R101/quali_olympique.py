def qualification(gender,pr100m,racewin,wc):
    """Vérifie si l'athlete peut se qualifier aux jeux olympique

    Args:
        gender (str): genre de la personne
        pr100m (int): record aux 100m
        racewin (int): Nombre de course gagné dans l'année
        wc (bool): Champion.ne du monde dans sa discpline

    Returns:
        bool: L'athlete est t'il qualifié aux jeux olympique
    """    
    res = False
    if gender == "h":
        if pr100m<12 and racewin >= 3 or wc == True:
            res = True
    elif pr100m<15 and racewin >= 3 or wc == True:
        res = True
    return res

def test_qualification():
    assert qualification("h",20,5,False)
    assert qualification("h",3,40,False)
    assert qualification("f",85,1,True)
    assert qualification("f",11,4,False)