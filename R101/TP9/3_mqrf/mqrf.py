
# ==========================
# La maison qui rend fou
# ==========================
mqrf1 = {"Abribus":"Astus", "Jeancloddus":"Abribus", "Plexus":"Gugus","Astus":None, "Gugus":"Plexus", "Saudepus":None}


def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    guichet_actuel = guichet
    while mqrf[guichet_actuel] is not None:
        print("Je vais au guichet "+mqrf[guichet_actuel])
        guichet_actuel = mqrf[guichet_actuel]
    print("C'est bon mon goat, le formulaire A_38 est guichet :")
    return guichet_actuel


def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    nbguichet = 1
    guichet_actuel = guichet
    while mqrf[guichet_actuel] is not None:
        print("Je vais au guichet "+mqrf[guichet_actuel])
        guichet_actuel = mqrf[guichet_actuel]
        nbguichet += 1
    print("C'est bon mon goat, le formulaire A_38 est guichet :")
    return (guichet_actuel,nbguichet)
print(quel_guichet_v2(mqrf1,"Jeancloddus"))

def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    

