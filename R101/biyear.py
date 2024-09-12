def biyear(year):
    """Vérifie si une année est bissextile 

    Args:
        year (int): valeur de l'année

    Returns:
        bool: Année bissextile ou pas
    """    
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0

def test_biyear():
    assert biyear(2024) == True
    assert biyear(1900) == False
    assert biyear(2004) == True
    assert biyear(1800) == False
            