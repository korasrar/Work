def biyear(year):
    res = False
    if year % 4 == 0 or year % 400 == 0:
        res = True
        if year % 100 == 0 :
            res = False
    return res

def test_biyear():
    assert biyear(2024) == True
    assert biyear(1900) == False
    assert biyear(2004) == True
    assert biyear(1800) == False
            