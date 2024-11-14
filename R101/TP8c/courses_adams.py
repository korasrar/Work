# liste dans tuple ? onjectif meme parametre (api)
def ajt_articlemorticia(courses,nom,prix):
    check = False
    for article in courses[0]:
        if article == nom:
            check = True
    if not check:
        courses[0].append(nom)
        courses[1].append(prix)
    else: 
        print("Article déja présent dans la liste de courses")

def sup_articlemorticia(courses,nom):
    check = False
    saveart = 0
    for i in range(len(courses[0])):
        if courses[0][i] == nom:
            check = True
            saveart = i
    if check:
        courses[0].pop(saveart)
        courses[1].pop(saveart)
    else : 
        print("Article pas présent dans la liste de courses")

def changepricemorticia(courses,nom,nvprix):
    check = False
    saveart = 0
    for i in range(len(courses[0])):
        if courses[0][i] == nom:
            check = True
            saveart = i
    if check:
        courses[1][i] = nvprix
    else :
        print("Article pas présent dans la liste de courses")

def totalpricemorticia(courses):
    total = 0 
    for prix in courses[1]:
        total += prix
    return total

def namearticle_maxmorticia(courses):
    saveprix = 0
    prixmax = 0
    for i in range(len(courses[1])):
        if prixmax < courses[1][i]:
            prixmax = courses[1][i]
            saveprix = i 
    return courses[0][saveprix]

# ------------------------------------------

def ajt_articleGomez(courses,nom,prix):
    check = False
    for i in range(0,len(courses),2):
        if nom == courses[i]:
            check = True
    if not check:
        courses.extend([nom,prix])
    else : 
        print("Article déja présent dans la liste de courses")

def sup_articleGomez(courses,nom):
    check = False
    for i in range(0,len(courses),2):
        if nom == courses[i]:
            check = True
    if check:
        courses.remove(nom)
        courses.pop(courses.index(nom)+1)
    else : 
        print("Article pas présent dans la liste de courses")

def changepriceGomez(courses,nom,nvprix):
    check = False
    for i in range(0,len(courses),2):
        if nom == courses[i]:
            check = True
    if check:
        courses[nom]=nvprix
    else :
        print("Article pas présent dans la liste de courses")

def totalpriceGomez(courses):
    f

def namearticle_maxGomez(courses):
    f

# ------------------------------------------

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

# -- EX3 -----------------------------------


# ------------------------------------------

def ajt_article(courses,nom,prix):
    f

def sup_article(courses,nom):
    f

def changeprice(courses,nom,nvprix):
    f

def totalprice(courses):
    f

def namearticle_max(courses):
    f