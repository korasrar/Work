"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    famillepokedex = set()
    for pokemon in pokedex:
        if pokemon[1] not in famillepokedex:
            famillepokedex.add(pokemon[1])
    return famillepokedex

def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nbpokemon = 0
    for pokemon in pokedex:
        if pokemon[1] == famille:
            nbpokemon += 1
    return nbpokemon

def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    frqfamille = {}
    for pokemon in pokedex:
        if pokemon[1] in frqfamille:
            frqfamille[pokemon[1]] += 1
        else:
            frqfamille[pokemon[1]] = 1
    return frqfamille

def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dicofrequence = frequences_famille(pokedex)
    dicofamille = {}
    for famille in dicofrequence.keys():
        enstemp = set()
        for pokemon in pokedex:
            if pokemon[1] == famille:
                enstemp.add(pokemon[0])
        dicofamille[famille] = enstemp
    return dicofamille

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    frqfamille = frequences_famille(pokedex)
    famillemax = ""
    nbmax = 0
    for famille,frq in frqfamille.items():
        if frq > nbmax:
            famillemax = famille
            nbmax = frq
    return famille

# ==========================
# Petites bêtes (la suite)
# ==========================

def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    famille = set()
    for fam in pokedex.values():
        famille.update(fam)
    return famille

def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    res = 0
    for type in pokedex.values():
        if famille in type:
            res += 1
    return res

def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    type_frequence = {}
    for famille in pokedex.values():
        for type in famille:
            if type in type_frequence:
                type_frequence[type] += 1
            else: 
                type_frequence[type] = 1
    return type_frequence

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dicofamille = {}
    for pokemon,famille in pokedex.items():
        for type in famille:
            if type not in dicofamille:
                dicofamille[type] = set()
            dicofamille[type].add(pokemon)
    return dicofamille

def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    dicofrequence = frequences_famille_v2(pokedex)
    res = 0 
    famillemax = ""
    for famille,val in dicofrequence.items():
        if val > res:
            res = val
            famillemax = famille
    return famillemax
