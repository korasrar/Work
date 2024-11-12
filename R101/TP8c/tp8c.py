def trouver_dans_liste(liste, cible):
    indice = 0
    check = False
    while indice < len(liste) and not check:
        if liste[indice] == cible :
            check = True
        indice += 1 
    return check

def cumuler_jusqu_a_seuil(dictionnaire, seuil):
    total = 0
    check = False
    ind = 0
    values = list(dictionnaire.values())
    while ind < len(values) and not check:
        total += values[ind]  
        if total >= seuil:
            check = True
        ind += 1
    return total
