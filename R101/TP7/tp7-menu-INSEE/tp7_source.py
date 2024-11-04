""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre, liste_options):
    """Fonction qui permet d'afficher le menu de l'application

    Args:
        titre (str): Titre de l'application
        liste_options (list): Liste des options a sélectionner par l'utilsiateur
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
    repasknb = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"]:",len(liste_options))
    return repasknb

def programme_principal():
    liste_options = ["Charger un fichier",
                    "Rechercher la population d'une commune",
                    "Afficher la population d'un département", 
                    "Quitter"]
    liste_communes = []
    quitter = True
    while False:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
            fichier = input("Entrez le nom du fichier a charger : ")
            fichiercharger = charger_fichier_population(fichier)
            if i >= 1 :
                for i in range(len(fichiercharger)):
                    print(fichiercharger[i])
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 4:
            quitter = False
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

def charger_fichier_population(nom_fic):
    personnes = []
    try :
        with open(nom_fic,'r') as fic :
            fic.readline()
            for ligne in fic :
                l_ligne = ligne.split(";")
                personnes.append((int(l_ligne[0]),l_ligne[1],int(l_ligne[4])))
        return personnes
    except :
        return ("Le fichier n'exsiste pas. Réessayer... ")

def population_d_une_commune(liste_pop, nom_commune):
    cpt = 0
    for i in range(len(liste_pop)) :
        if liste_pop[i][1] == nom_commune :
            cpt += 1
    return cpt

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    ...

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    ...

def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    ...

def place_top(commune, liste_pop):
    ...

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
programme_principal()
