import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions
def afficher_menu(titre, liste_options):
    """Fonction qui permet d'afficher le menu de l'application

    Args:
        titre (str): Titre de l'application
        liste_options (list): Liste des options a sélectionner par l'utilisateur
    """    
    print("+-------------------------+")
    print("|",titre,"|")
    print("+-------------------------+")
    for i in range(len(liste_options)):
        print(i+1," -> ",liste_options[i])

def demander_nombre(message, borne_max):
    rep = int(input(message))
    if str(rep).isdecimal() and rep <= borne_max:
        return int(rep)
    return None

def menu(titre, liste_options):
    afficher_menu(titre,liste_options)
    repasknb = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"] : ",len(liste_options))
    return repasknb

# ici votre programme principal
def programme_principal():
    liste_options = [
                "Bilan Carbone pour un certain mois",
                "Bilan Carbone pour une certaine année",
                "Liste activité d'une certaine personne",
                "Activité la plus polluante d'une certaine personne",
                "Pourcentage de personne pratiquant une activité",
                "Tendance",
                "Sauvegarder liste en fichier csv",
                "Quitter"]
    liste_chargée = []
    fichierchargé = False
    quitter = False
    while not fichierchargé :
        try:
            bc.charger_activites(input("Veuillez entrer le nom d'un fichier csv : "))
        except:
            print("Fichier inexistant, Recommencer !")
        else:
            fichierchargé = True
            print("FICHIER CHARGER")
    while not quitter:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])

        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])

        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])

        elif rep == len(liste_options):
            quitter = True
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

programme_principal()
