def sommepair(liste_nb):
    """Fait la somme des nombres pairs d'une liste

    Args:
        liste_nb (list): liste de nombres

    Returns:
        int: somme des nombres pairs de la liste
    """    
    somme = 0
    for n in liste_nb :
        if n%2 == 0 : 
            somme += n
    return somme 

def test_sommepair():
    assert sommepair([12,13,6,5,7]) == 18
    assert sommepair([2,2,2,2,2,2,2,2]) == 16
    assert sommepair([]) == 0
    assert sommepair([3,5,7,-2,5,1]) == -2
    
#--------------------------------------------------

def lastvoyelle(mot):
    """Cherche la dernière voyelle dans un mot

    Args:
        mot (str): un mot en minuscule only

    Returns:
        str or Nonetype: la dernière voyelle du mot
    """    
    voyelle = None
    for l in mot :
        if l in "aeiouy" :
            voyelle = l
    return voyelle

def test_lastvoyelle():
    assert lastvoyelle("buongiorno") == "o"
    assert lastvoyelle("") is None
    assert lastvoyelle("bonjour") == "u"
    assert lastvoyelle("psdvll") is None
    
#--------------------------------------------------

def propnb_negatif(liste_nb):
    """Calcule la proportion de nombres negatifs dans une liste

    Args:
        liste_nb (list): liste de nombres

    Returns:
        float or Nonetype: proportion de nombres negatifs
    """    
    proportion = None
    for n in liste_nb :
        total += 1
        if n < 0 :
            negatif += 1
    if negatif < 0
        proportion = negatif/total
    return proportion

def test_propnb_negatif():
    assert 
