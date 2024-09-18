# exercice 1
def majopairs(entree):
    """Vérifie si il y a une majorité de nombres pairs dans la liste

    Args:
        entree (list): Liste de nombres

    Returns:
        bool: Nombre de chiffre pairs supérieur aux autres
    """
    pairs = 0
    impairs = 0
    # au début de chaque tour de boucle
    #  A COMPLETER
    for nombres in entree:
        if nombres % 2 == 0:
            pairs += 1
        else:
            impairs += 1
    return pairs >= impairs


def test_majopairs():
    assert majopairs([1,2,1,6,6,2,1]) == True
    assert majopairs([2,2,2,2,2,2,2]) == True
    assert majopairs([5,5,5,5,5,5,5]) == False
    assert majopairs([6,6,6,6,6,6,6]) == True


# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    res = None
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur
    for elem in liste_nombres :
        if elem > valeur :
            res = elem
    if res != None :
        for elem in liste_nombres :
            if valeur < elem < res:
                res = elem
    return res

def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None


# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ''
    c2 = ''
    # au début de chaque tour de boucle
    # c1 vaut
    # c2 vaut
    # resultat vaut  
    for c2 in phrase:
        if c1 == ' ' and c2 != ' ':
            resultat = resultat + 1
        c1 = c2
    return resultat+1
print(nb_mots(" ce  test ne  marche pas ") == 5)


def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots("houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

