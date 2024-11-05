# Codé par Papy Force X, jeune padawan de l'informatique
def longueur_ok(mdp):
    if len(mdp) < 8:
        return False
    return True

def chiffre_ok(mdp):
    for lettre in mdp:
        if lettre.isdigit():
            return True
    return False

def sans_espace(mdp):
    for lettre in mdp:
        if lettre == " ":
            return False
    return True

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if not longueur_ok(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins 8 caractères")
        if not chiffre_ok(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins un chiffre")
        if not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")	 
        if sans_espace(mot_de_passe) and longueur_ok(mot_de_passe) and chiffre_ok(mot_de_passe):
            mot_de_passe_correct = True        
    print("Votre mot de passe est correct")
    return mot_de_passe

dialogue_mot_de_passe()