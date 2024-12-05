"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for poke in pokedex:
        if poke[0] == pokemon:
            return True
    return False

def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    typeattaque = set()
    for poke in pokedex:
        if poke[0] == pokemon:
            typeattaque.add(poke[1])
    return typeattaque

def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    res = 0
    for typeattaque in pokedex:
        if typeattaque[1] == attaque:
            res += 1
    return res


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    frequence = {}
    for poke in pokedex:
        if poke[1] in frequence:
            frequence[poke[1]] += 1
        else:
            frequence[poke[1]] = 1
    typemax = ""
    resmax = 0
    for typeattaque,val in frequence.items():
        if resmax < val:
            typemax = typeattaque
            resmax = val
    return typemax


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    if pokemon in pokedex.keys():
        return True
    return False


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    return pokedex[pokemon]


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    res = 0
    for typeattaque in pokedex.values():
        if attaque in typeattaque:
            res += 1
    return res

def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dico = {}
    for typeattaque in pokedex.values():
        for attaque in typeattaque:
            if attaque in dico:
                dico[attaque] += 1
            else:
                dico[attaque] = 1
    typemax = ""
    resmax = 0
    for typeattaque,val in dico.items():
        if resmax < val:
            typemax = typeattaque
            resmax = val
    return typemax

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for allpokemon in pokedex.values():
        if pokemon in allpokemon:
            return True
    return False


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    typeattaque = set()
    for attaque,allpokemon in pokedex.items():
        if pokemon in allpokemon:
            typeattaque.add(attaque)
    return typeattaque


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    if attaque in pokedex :
        return len(pokedex[attaque])
    return 0


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    attaquemax = ""
    pokemonmax = 0
    for attaque,pokemon in pokedex.items():
        if len(pokemon) > pokemonmax:
            pokemonmax = len(pokemon)
            attaquemax = attaque
    return attaquemax
    #return max(list(len(pokedex.keys())))

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    pokedexv2  = {}
    for pokemon,typeattaque in pokedex_v1:
        if pokemon not in pokedexv2:
            pokedexv2[pokemon] = set()
        pokedexv2[pokemon].add(typeattaque)
    return pokedexv2

# Version 2 ==> Version 3

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """

