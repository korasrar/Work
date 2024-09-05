m = ""

def algo2(m):
    res = 0
    for caractere in m:
        if caractere in ["a","e","i","o","u","y"]:
            res = res+1
        else:
            res = res-1
    return res>0
print(algo2("aezd"))

def test_algo2():
    assert algo2("aeizd") == True