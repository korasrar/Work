def nbval_3ite(liste, valeur):
    """Retourne le nombre de valeur parcouru la liste a partir du 
    moment ou il y aura plus de 3 itérations de la valeurs choisi dans une liste

    Args:
        liste (list): liste de valeur
        valeur (int): valeur

    Returns:
        Bool or Int: None ou cpt si la valeur apparée plus de 3 fois
    """
    cpt = 0
    equalval = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            equalval += 1
            if equalval > 3:
                return cpt
        cpt += 1
    return None
#print(mystere([12, 20, 8, 48, 20, 418, 20, 17, 20, 87], 20))

def test_nbval_itevaleurs():
    assert nbval_itevaleurs([],) == None
    assert nbval_itevaleurs([],) == None
    assert nbval_itevaleurs([],) == None
    assert nbval_itevaleurs([],) == None

# --------------------------------------
# Exercice n°2
# --------------------------------------

def indfirstint(phrase) :
    for i in range(len(phrase)) :
        if phrase[i].isnumeric() :
            return i
    return None
#print(indfirstint("shinjiikari"))

def test_indfirstint():
    assert indfirstint("") == None
    assert indfirstint("") == None
    assert indfirstint("") == None
    assert indfirstint("") == None    

def cityfinder(liste_ville,popu,ville) : 
    for i in range(len(liste_ville)) :
        if liste_ville[i] == ville :
            return popu[i]
    return None
#print(cityfinder(["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux","Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"],[45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,136463,  25725],"Blois"))

# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
liste_villes = ["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux","Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"]
population = [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,136463,  25725]

# --------------------------------------
# Exercice n°3
# --------------------------------------

def listcroissant(list_nb):
    for i in range(1,len(list_nb)):
        if list_nb[i] > list_nb[i-1] :
            res = True
        else :
            return False
    return res
#print(listcroissant([1,2,3,4,5,6,7,8,9]))

def test_listcroissant():
    assert listcroissant([]) == False
    assert listcroissant([]) == False
    assert listcroissant([]) == False
    assert listcroissant([]) == False

def sommesupvaleurs(list_nb,valeur) :
    somme = 0
    for i in range(len(list_nb)):
        somme += list_nb[i]
    if somme > valeur :
        return True
    return False
#print(sommesupvaleurs([1,4,1,2,3,4],6))

def test_sommesupvaleurs():
    assert sommesupvaleurs([],) == True
    assert sommesupvaleurs([],) == True
    assert sommesupvaleurs([],) == True
    assert sommesupvaleurs([],) == True

def verifemail(email):
    if phrase[0] != "@" and phrase[-1] != "." :   
        for i in range(len(email)) :
            f
    return False

# ---------------------------------------
# Exercice n°4 
# ---------------------------------------
# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']
