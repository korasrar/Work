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
    """Demande le nombre de l'option a chosir et retourne None si elle existe pas 

    Args:
        message (str): Le message qui s'affichera dans le terminal
        borne_max (int): Le nombre de la dernière option

    Returns:
        int or NoneType: la valeur de l'option ou None
    """    
    rep = int(input(message))
    if str(rep).isdecimal() and rep <= borne_max:
        return int(rep)
    return None

def menu(titre, liste_options):
    """Affiche le menu et la demande de selection de l'option

    Args:
        titre (str): Titre du menu
        liste_optionsmenu (liste): La liste d'options

    Returns:
        str: La demande de selection
    """    
    afficher_menu(titre,liste_options)
    repasknb = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"] : ",len(liste_options))
    return repasknb

def askname(liste_chargee):
    """Demande le nom d'une personne et vérifie si elle est dans la liste chargée

    Args:
        liste_chargee (liste): Liste chargée par l'utilisateur

    Returns:
        str: Le nom de la personne
    """    
    check = False
    while not check:
        name = input("Entrer le nom de la personne : ")
        for activite in liste_chargee:
            if name == activite[0]:
                check = True
        if not check :
            print("Nom introuvable dans la liste. Réessayer.")
    return name

def askdate(liste_chargee):
    """Demande la date et vérifie si elle est dans la liste chargée

    Args:
        liste_chargee (liste): Liste chargée par l'utilisateur

    Returns:
        str: La date
    """  
    check = False
    while not check:
        date = input("Entrer la date a chercher : ")
        for activite in liste_chargee:
            if date == activite[1]:
                check = True
        if not check :
            print("Date introuvable dans la liste. Réessayer.")
    return date

def asktype(liste_chargee):
    """Demande le type et vérifie si elle est dans la liste chargée

    Args:
        liste_chargee (list): Liste chargée par l'utilisateur

    Returns:
        str: Le type
    """  
    check = False
    while not check:
        type = input("Entrer le type a chercher : ")
        for activite in liste_chargee:
            if type == activite[3]:
                check = True
        if not check :
            print("Type introuvable dans la liste. Réessayer.")
    return type

def loadfile():
    """Demande le fichier .csv a charger et le charge si il existe

    Returns:
        list: La liste créer a partir du contenu du fichier
    """    
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
    """Demande le filtre a appliqué pour une future recherche dans la liste chargée

    Args:
        liste_options (_type_): Liste des filtres
        liste_chargee (_type_): Liste chargée par l'utilisateur

    Returns:
        int: Numéro de l'option sélectioner 
    """    
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

def requestfiltre(liste_options,liste_chargee):
    if input("Voulez vous appliquer un filtre ? (y/n) : ") == 'y':
        return askfiltre(liste_options,liste_chargee)
    else :
        return liste_chargee

# ici votre programme principal
def programme_principal():
    liste_optionsmenu = [
                "Bilan Carbone pour septembre",
                "Liste activité avec filtre",
                "Activité la plus polluante",
                "Moyenne émission de carbone en septembre",
                "Pourcentage de personne pratiquant une activité",
                "Durée moyenne de pratique",
                "Recherche d'une actvité",
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
            refiltre = requestfiltre(liste_optionsfiltre,liste_chargee)
            print(bc.max_emmission(refiltre))
        elif rep == 4: # MOYENNE EMISSION SEPTEMBRE ------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            refiltre = requestfiltre(liste_optionsfiltre,liste_chargee)
            print("Moyenne d'emission de la liste (filtré ou non) sur septembre : ",bc.cumul_emmissions(refiltre)//len(refiltre),"g")
        elif rep == 5: # POURCENTAGE ACTIVITE ------------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            type = asktype(liste_chargee)
            pourcentage = (len(bc.filtre(liste_chargee,3,type))/len(liste_chargee))*100
            print(round(pourcentage,2),"% des activitées qui sont de",type)
        elif rep == 6: # DUREE MOYENNE DE PRATIQUE -------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            type = asktype(liste_chargee)
            tempsmoyen = bc.cumul_temps_activite(liste_chargee,bc.co2_minute)/len(bc.filtre(liste_chargee,3,type))
            print("La durée moyenne de pratique des activitées de ",type," est de : ",round(tempsmoyen,2)," min")
        elif rep == 7: # RECHERCHE D'UNE ACTIVITE --------------------------
            print("Vous avez choisi", liste_optionsmenu[rep - 1])
            name = askname(liste_chargee)
            type = asktype(liste_chargee)
            date = askdate(liste_chargee)
            recherche = bc.recherche_activite_dichotomique(name,date,type,liste_chargee)
            if recherche != None :
                print("Voici l'activité qui correspond a vos critères : ",recherche)
            else :
                print("Aucune activité trouvé.")
        elif rep == 8: # CHARGER NOUVEAU FICHIER ---------------------------
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
