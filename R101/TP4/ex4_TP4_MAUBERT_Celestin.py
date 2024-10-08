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
    liste_word = []
    for i in range(len(liste_all)):
        if lettre == liste_all[i][0] : 
            liste_word.append(liste_all[i])
    return liste_word

def test_searchword():
    assert searchword(["salut","hello","hallo","ciaohi","hola"],"h") == ['hello', 'hallo', 'hola']
    assert searchword(["rei","ayanami","asuka","langley","shinji","ikari"],"a") == ['ayanami','asuka']
    assert searchword(["alut","aurevoir","avoir","littérature"],"s") == []
    assert searchword([],"z") == []