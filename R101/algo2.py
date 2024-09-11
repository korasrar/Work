m = ""

def algo2(m):
    """algo2 permet de savoir si il y a une majorite de voyelles dans le mot

    Args:
        m (str): mot avec voyelles ou non

    Returns:
        bool: voyelles > 0 ou pas
    """    
    res = 0
    for caractere in m:
        if caractere in ["a","e","i","o","u","y"]:
            res = res+1
        else:
            res = res-1
    return res>0

def test_algo2():
    assert algo2("aeizd") == True
    assert algo2("aezd") == False
    assert algo2("klhjg") == False
    assert algo2("aeiouy") == True