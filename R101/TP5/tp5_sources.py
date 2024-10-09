def mystere(liste, valeur):
    """[summary]

    Args:
        liste ([type]): [description]
        valeur ([type]): [description]

    Returns:
        [type]: [description]
    """
    xxx = 0
    yyy = 0
    for elem in liste:
        if elem == valeur:
            yyy += 1
            if yyy > 3:
                return xxx
        xxx += 1
    return None


mystere([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux",
                "Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,
              136463,  25725]

# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
