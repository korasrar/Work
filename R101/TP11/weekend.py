# EX1 ---------------------------------

week_end_mai = {'Pierre':[12,70,10],'Paul':[100],'Marie':[15],'Anna':[]}
week_end_juin = {'Pierre':[15,12,8,3],'Marie':[20,34],'Anna':[52],'Beatrice':[8]}

def affiche_bilan_financier(week_end):
    prixtotal = 0
    for prix in week_end.values():
        prixtotal+=sum(prix)
    prixparpersonne = prixtotal/len(week_end)
    for personne in week_end:
        prixarendre = prixparpersonne-sum(week_end[personne])
        if prixarendre < 0:
            print(f"{personne} doit recevoir {abs(prixarendre)}")
        else:
            print(f"{personne} doit verser {prixarendre}")
print(affiche_bilan_financier(week_end_mai))

# EX2 ---------------------------------

ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida','Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri','Gaston':'Beatrice','Henri':'Firmin'}

def amour_reciproque(dico_amoureux):
    res = []
    for personne in dico_amoureux:
        if personne == dico_amoureux[dico_amoureux[personne]] and (dico_amoureux[personne],personne) not in res :
            res.append((personne,dico_amoureux[personne]))
    return res
print(amour_reciproque(ATM))

def soupirants(dico_amoureux,nom):
    res = []
    for personne in dico_amoureux:
        if nom == dico_amoureux[personne]:
            res.append(personne)
    return res
print(soupirants(ATM,'Cesar'))

# EX3 ---------------------------------

def sous_matrice(matrice,nb_lignes,nb_colonnes,position_haut,position_gauche):
    