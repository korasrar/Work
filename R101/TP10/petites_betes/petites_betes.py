""" Correction Exercice 4 petites bêtes TP 10 """

ma_liste_pokemon =[("Bulbizarre", {"Plante", "Poison"}, "001. png"),
                   ("Herbizarre", {"Plante", "Poison"}, "002. png"),
                   ("Abo", {"Poison"}, "023. png"),
                   ("Jungko", {"Plante"}, "254. png")]

def pokemon_par_famille(liste_pokemon):
    """ détermine le dictionnaire de clefs : nom de famille
        et de valeurs l'ensemble des pokemon de cette famille

    Args:
        liste_pokemon (list): liste de tuples (nom_poke, ensemble des familles, image)

    Returns:
        dict: le dictionnaire nom_famille ensemble des noms de pokemon de cette famille
    """
    nom_famille = {}
    for pokemon in liste_pokemon:
        for famille in pokemon[1]:
            if famille not in nom_famille:
                nom_famille[famille] = set()
        nom_famille[famille].add(pokemon)
    return nom_famille
print(pokemon_par_famille(ma_liste_pokemon))

def test_pokemon_par_famille():
    ...
    