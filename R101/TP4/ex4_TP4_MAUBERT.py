# --------------------------------------
# EXERCICE N°4 du TP4
# Auteur : Célestin MAUBERT
# Groupe : 11A
# --------------------------------------

def searchword(liste_all,lettre):
    """Liste les mots commencent par une certaine lettre

    Args:
        liste_all (list): Liste avec tout les mots
        lettre (str): Lettre par laquel le mot doit commencer

    Returns:
        list: Liste des mots qui commence par la lettre choisie
    """    
    mots = ""
    liste_word = []
    for i in range(len(liste_all)):
        mots = liste_all[i]
        if lettre == mots[0] : 
            liste_word.append(mots)
    return liste_word

def test_searchword():
    assert searchword(["salut","hello","hallo","ciao","hola"],"h") == ['hello', 'hallo', 'hola']
    assert searchword(["rei","ayanami","asuka","langley","shinji","ikari"],"a") == ['ayanami','asuka']
    assert searchword(["salut","aurevoir","savoir","littérature"],"s") == ['salut','savoir']