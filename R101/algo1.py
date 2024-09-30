a = 0
b = 0
c = 0
d = 0

def algo1(a,b,c,d):
    """lgo1 permet de trouver le nombres le plus petit entre a,b,c,d

    Args:
        a (int): 
        b (int): 
        c (int): 
        d (int): 

    Returns:
        int: la variables la plus petite
    """    
    if a < b:
        res = a
    else:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

def test_algo1():
    assert algo1(3,8,4,7) == 3
    assert algo1(8,7,4,3) == 3
    assert algo1(3,12,4,5) == 3
    assert algo1(15,3,2,9) == 2
