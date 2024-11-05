# Codé par Papy Force X, jeune padawan de l'informatique
def longueur_ok(mdp):
    """Vérifie si le mdp fait au moins 8 caractères
    Args:
        mdp (str): mot de passe rentré par l'utilisateur
    Returns:
        bool: True = >=8 False = <8
    """    
    if len(mdp) < 8:
        return False
    return True

def chiffre_ok(mdp):
    cpt = 0
    for lettre in mdp:
        if lettre.isdigit():
            return True
    return False

def chiffre_suite(mdp):
    for i in range(len(mdp)-1):
        if mdp[i].isdigit() and mdp[i+1].isdigit():
            return False
    return True

def min3chiffres(mdp):
    cpt = 0
    for lettre in mdp:
        if lettre.isdigit():
            cpt += 1
    if cpt < 2 :
        return False
    return True

def chiffrelepluspetit(mdp):
    chiffremin = '10'
    cpt = 0
    for carac in mdp:
        if carac.isdigit():
            if chiffremin > carac:
                chiffremin = carac
    for carac in mdp:
        if chiffremin == carac :
            cpt += 1
        if cpt > 1:
            return False
    return True

def sans_espace(mdp):
    """Vérifie si le mdp n'a pas d'espaces
    Args:
        mdp (str): mot de passe rentré par l'utilisateur
    Returns:
        bool: True = pas d'espaces, False = espaces
    """    
    for lettre in mdp:
        if lettre == " ":
            return False
    return True

def savemdp(mdp,login):
    with open("R101/TP8/mdpUltraSecret.txt", "w") as fic:
        fic.write(login+":"+mdp+"\n")

def veriflogin(nomfichier,login,mdp):
    res={}
    with open(nomfichier, "r") as fic:
        for login in fic:
            l_login = activite.strip().split(",")
            res[l_login[0]]=l_login[1]
    for log in res.keys():
        if login == log:

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if not longueur_ok(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins 8 caractères")
        if not chiffre_ok(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins un chiffre")
        if not chiffre_suite(mot_de_passe):
            print("Votre mot de passe doit comporter au moins trois chiffres")
        if not min3chiffres(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter deux chiffres consécutifs")
        if not chiffrelepluspetit(mot_de_passe):
            print("Le chiffre le plus petit doit apparaître une seule fois")
        if not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace") 
        if sans_espace(mot_de_passe) and longueur_ok(mot_de_passe) and chiffre_ok(mot_de_passe) and chiffre_suite(mot_de_passe) and min3chiffres(mot_de_passe) and chiffrelepluspetit(mot_de_passe):
            mot_de_passe_correct = True
    savemdp(mot_de_passe,login)
    print("Votre mot de passe est correct et sauvegardé")
    return mot_de_passe

dialogue_mot_de_passe()