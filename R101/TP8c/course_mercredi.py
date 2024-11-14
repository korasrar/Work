def ajt_articleMercredi(courses,nom,prix):
    check = False
    for article in courses.keys():
        if nom == article:
            check = True
    if not check:
        courses[nom]=prix
    else : 
        print("Article déja présent dans la liste de courses")

def sup_articleMercredi(courses,nom):
    check = False
    for article in courses.keys():
        if nom == article:
            check = True
    if check:
        del courses[nom]
    else : 
        print("Article pas présent dans la liste de courses")

def changepriceMercredi(courses,nom,nvprix):
    check = False
    for article in courses.keys():
        if nom == article:
            check = True
    if check:
        courses[nom]=nvprix
    else :
        print("Article pas présent dans la liste de courses")

def totalpriceMercredi(courses):
    total = 0 
    for prix in courses.values():
        total += prix
    return total

def namearticle_maxMercredi(courses):
    prixmax = 0
    articlemax = 0
    for article, prix in courses.items():
        if prixmax < prix :
            prixmax = prix
            articlemax = article
    return articlemax

def askprice():
    check = False
    while not check:
            try:
                prix = int(input("Entrer le prix de l'article : "))
            except:
                print("Le prix doit forcément être un nombre ! Retry")
            else:
                check = True
    return prix

def creerlistecourse():
    courses = {}
    quitter = False
    while not quitter:
        nomarticle = input("Entrer le nom de l'article : ")
        prix = askprice()
        courses[nomarticle] = prix
        if input("Voulez vous encore ajouter un article ? (y/n) : ") == "n":
            quitter = True
    return courses
print(creerlistecourse())

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
    try :    
        rep = int(input(message))
        if str(rep).isdecimal() and rep <= borne_max:
            return int(rep)
        return None
    except ValueError:
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

def programmepincipal():
    liste_options=[
        "",
        "",
        ""
        ]
    quitter = False
    while not quitter:
        rep = menu("GESTIONNAIRE DE COURSES")