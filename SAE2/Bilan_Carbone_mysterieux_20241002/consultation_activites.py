import bilan_carbone as bc

# Ici vos fonctions dédiées aux interactions
def afficher_menu(titre, liste_options):
    """Fonction qui permet d'afficher le menu de l'application

    Args:
        titre (str): Titre de l'application
        liste_optionsmenu (list): Liste des options a sélectionner par l'utilisateur
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

def menu(titre, liste_optionsmenu):
    afficher_menu(titre,liste_optionsmenu)
    repasknb = demander_nombre("Entrez votre choix [1-"+str(len(liste_optionsmenu))+"] : ",len(liste_optionsmenu))
    return repasknb

def askname(liste_chargee):
    check = False
    while not check:
        name = input("Entrer le nom de la personne : ")
        for activite in liste_chargee:
            if name == activite[0]:
                check = True
        print("Nom introuvable dans la liste. Réessayer.")
    return name

def askdate(liste_chargee):
    check = False
    while not check:
        date = input("Entrer la date a chercher : ")
        for activite in liste_chargee:
            if date == activite[1]:
                check = True
        print("Date introuvable dans la liste. Réessayer.")
    return date

def asktype(liste_chargee):
    check = False
    while not check:
        type = input("Entrer le type a chercher : ")
        for activite in liste_chargee:
            if type == activite[3]:
                check = True
        print("Type introuvable dans la liste. Réessayer.")
    return type

def loadfile():
    liste_chargee = []
    fichierchargé = False
    while not fichierchargé :
        try:
            liste_chargee = bc.charger_activites(input("Veuillez entrer le nom d'un fichier csv : "))
        except:
            print("Fichier inexistant, Recommencer !")
        else:
            fichierchargé = True
            print("FICHIER CHARGER !")
            return liste_chargee

def askfiltre(liste_options,liste_chargee):
    quitter = False
    while not quitter :
        rep = menu("CHOIX DU FILTRE",liste_options)
        if rep is None:
            print("Ce filtre n'existe pas")
        elif rep == 1:
            filtre = askname(liste_chargee)
            res = bc.filtre(liste_chargee,0,filtre)
            quitter = True
        elif rep == 2:
            filtre = askdate(liste_chargee)
            res = bc.filtre(liste_chargee,1,filtre)
            quitter = True
        elif rep == 3:
            filtre = asktype(liste_chargee)
            res = bc.filtre(liste_chargee,3,filtre)
            quitter = True
    return res


# ici votre programme principal
def programme_principal():
    liste_optionsmenu = [
                "Bilan Carbone pour septembre",
                "Liste activité avec filtre",
                "Activité la plus polluante",
                "Moyenne émission de carbone en septembre",
                "Pourcentage de personne pratiquant une activité",
                "Tendance",
                "Charger un nouveaux fichier",
                "Quitter"]
    liste_optionsfiltre = [
                "Prénom",
                "Date (year-month-day)",
                "Type"]
    liste_chargee = []
    saveliste = []
    listerfusion = []
    quitter = False
    liste_chargee = loadfile()
    while not quitter:
        rep = menu("MENU DE MON APPLICATION", liste_optionsmenu)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1: # BILAN CARBONE MOIS DE SEPTEMBRE -------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            nom = askname(liste_chargee)
            print("Bilan carbone de ",nom," : ",bc.cumul_emmissions(bc.filtre(liste_chargee,0,nom)),"g")
        elif rep == 2: # LISTE ACTIVITE ------------------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            listefiltre = askfiltre(liste_optionsfiltre,liste_chargee)
            print(listefiltre)
            saveliste = listefiltre
        elif rep == 3: # ACTIVITE LA PLUS POLLUANTE ------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            nom = askname(liste_chargee)
            print(bc.max_emmission(bc.filtre(liste_chargee,0,nom)))
        elif rep == 4: # MOYENNE EMISSION SEPTEMBRE ------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            nom = askname(liste_chargee)
            filtre = bc.filtre(liste_chargee,0,nom)
            print("Moyenne de",nom,"sur septembre : ",bc.cumul_emmissions(filtre)//len(filtre),"g")
        elif rep == 5: # POURCENTAGE ACTIVITE ------------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            type = asktype(liste_chargee)
            pourcentage = (len(bc.filtre(liste_chargee,3,type))/len(liste_chargee))*100
            print(round(pourcentage,2),"% des activitées qui sont de",type)
        elif rep == 6: # TENDANCE ------------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
        elif rep == 7: # CHARGER NOUVEAU FICHIER ---------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            loadfile()
        elif rep == len(liste_optionsmenu):
            quitter = True
        if saveliste != []:
            if input("Voulez vous sauvegarder la liste créer dans un fichier csv ? (y/n) : ") == 'y':
                bc.sauver_activites(input("Entrer le nom du fichier (oublier pas le .csv) : "),saveliste)
                print("Fichier sauvegarder !")
        saveliste = []
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

programme_principal()
