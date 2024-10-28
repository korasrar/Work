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
        print("[",i+1,"]",liste_options[i])

def demander_nombre(message, borne_max):
    rep = int(input(message))
    if str(rep).isdecimal() and rep <= borne_max:
        return int(rep)
    return None

def menu(titre, liste_options):
    afficher_menu(titre,liste_options)
    repasknb = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"] : ",len(liste_options))
    return repasknb

def askname(liste_chargée):
    while True:
        name = input("Entrer le nom de la personne : ")
        for activite in liste_chargée:
            if name == activite[0]:
                return name
        print("Nom introuvable dans la liste. Réessayer.")

def asktype(liste_chargée):
    while True:
        type = input("Entrer le type a cherhcer : ")
        for activite in liste_chargée:
            if type == activite[3]:
                return type
        print("Type introuvable dans la liste. Réessayer.")

def loadfile():
    fichierchargé = False
    while not fichierchargé :
        try:
            liste_chargée = bc.charger_activites(input("Veuillez entrer le nom d'un fichier csv : "))
        except:
            print("Fichier inexistant, Recommencer !")
        else:
            fichierchargé = True
            print("FICHIER CHARGER !")


# ici votre programme principal
def programme_principal():
    liste_options = [
                "Bilan Carbone pour septembre",
                "Liste activité",
                "Activité la plus polluante",
                "Moyenne émission de carbone en septembre",
                "Pourcentage de personne pratiquant une activité",
                "Tendance",
                "Charger un nouveaux fichier",
                "Quitter"]
    liste_chargée = []
    saveliste = []
    quitter = False
    loadfile()
    while not quitter:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1: # BILAN CARBONE MOIS DE SEPTEMBRE -------------------
            print("Vous avez choisi", liste_options[rep - 1])
            nom = askname(liste_chargée)
            print("Bilan carbone de ",nom," : ",bc.cumul_emmissions(bc.filtre(liste_chargée,0,nom)),"g")
        elif rep == 2: # LISTE ACTIVITE ------------------------------------
            print("Vous avez choisi", liste_options[rep - 1])
            nom = askname(liste_chargée)
            print(bc.filtre(liste_chargée,0,nom))
            saveliste = bc.filtre(liste_chargée,0,nom)
        elif rep == 3: # ACTIVITE LA PLUS POLLUANTE ------------------------
            print("Vous avez choisi", liste_options[rep - 1])
            nom = askname(liste_chargée)
            print(bc.max_emmission(bc.filtre(liste_chargée,0,nom)))
        elif rep == 4: # MOYENNE EMISSION SEPTEMBRE ------------------------
            print("Vous avez choisi", liste_options[rep - 1])
            nom = askname(liste_chargée)
            filtre = bc.filtre(liste_chargée,0,nom)
            print("Moyenne de",nom,"sur septembre : ",bc.cumul_emmissions(filtre)//len(filtre),"g")
        elif rep == 5: # POURCENTAGE ACTIVITE ------------------------------
            print("Vous avez choisi", liste_options[rep - 1])
            type = asktype(liste_chargée)
            print((len(bc.filtre(liste_chargée,3,type))//len(liste_chargée))*100,"% des activitées qui sont de",type)
        elif rep == 6: # TENDANCE ------------------------------
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 7: # CHARGER NOUVEAU FICHIER ---------------------------
            print("Vous avez choisi", liste_options[rep - 1])
            loadfile()
        elif rep == len(liste_options):
            quitter = True
        if saveliste != []:
            if input("Voulez vous sauvegarder la liste créer dans un fichier csv ? (y/n) : ") == 'y':
                bc.sauver_activites(input("Entrer le nom du fichier (oublier pas le .csv) : "),saveliste)
                print("Fichier sauvegarder !")
        saveliste = []
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

programme_principal()
