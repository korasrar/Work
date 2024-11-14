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

def menu():
    

def programmepincipal():
    f