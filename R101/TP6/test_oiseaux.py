import oiseaux
# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_recherche_oiseau():
    assert oiseaux.recherche_oiseau('Test',oiseaux.oiseaux)== None
    assert oiseaux.recherche_oiseau('Merle',oiseaux.oiseaux)== ("Merle", "Turtidé")
    assert oiseaux.recherche_oiseau('Moineau',oiseaux.oiseaux)== ("Moineau", "Passereau")
    assert oiseaux.recherche_oiseau('Pie',oiseaux.oiseaux)== ("Pie", "Corvidé")

def test_recherche_par_famille():
    assert oiseaux.recherche_par_famille('Test',oiseaux.oiseaux)== None
    assert oiseaux.recherche_par_famille('Picidae',oiseaux.oiseaux)== ['Pic vert']
    assert oiseaux.recherche_par_famille('Passereau',oiseaux.oiseaux)== ['Moineau','Mésange','Pinson','Rouge-gorge']
    assert oiseaux.recherche_par_famille('Turtidé',oiseaux.oiseaux)== ['Merle']

def test_oiseau_le_plus_observe():
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations1)=="Moineau"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations2)=="Tourterelle"
    assert oiseaux.oiseau_le_plus_observe(oiseaux.observations3)=="Mésange"
    assert oiseaux.oiseau_le_plus_observe([])==None

def test_est_liste_observations():
    assert oiseaux.est_liste_observations(oiseaux.observations1)== True
    assert oiseaux.est_liste_observations(oiseaux.observations2)== False
    assert oiseaux.est_liste_observations(oiseaux.observations3)== True

def test_max_observations():
    assert oiseaux.max_observations(oiseaux.observations1)==5
    assert oiseaux.max_observations(oiseaux.observations2)==5
    assert oiseaux.max_observations(oiseaux.observations3)==4

def test_moyenne_oiseaux_observes():
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations1)==3
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations2)==2.5
    assert oiseaux.moyenne_oiseaux_observes(oiseaux.observations3)==16/6

def test_total_famille():
    assert oiseaux.total_famille(oiseaux.observations1,oiseaux.oiseaux,"Turtidé")==2
    assert oiseaux.total_famille(oiseaux.observations2,oiseaux.oiseaux,"Passereau")==8
    assert oiseaux.total_famille(oiseaux.observations3,oiseaux.oiseaux,"Corvidé")==2
    assert oiseaux.total_famille(oiseaux.observations1,oiseaux.oiseaux,"Picidae")==1


def test_construire_liste_observations():
    assert oiseaux.construire_liste_observations(oiseaux.comptage1,oiseaux.oiseaux)==[('Merle', 2), ('Moineau', 5), ('Mésange', 0), ('Pic vert', 1), ('Pie', 2), ('Pinson', 0), ('Rouge-gorge', 3), ('Tourterelle', 5)]
    assert oiseaux.construire_liste_observations(oiseaux.comptage2,oiseaux.oiseaux)==[('Merle', 2), ('Moineau', 1), ('Mésange', 3), ('Pic vert', 0), ('Pie', 0), ('Pinson', 3), ('Rouge-gorge', 5), ('Tourterelle', 1)]
    assert oiseaux.construire_liste_observations(oiseaux.comptage3,oiseaux.oiseaux)==[('Merle', 0), ('Moineau', 0), ('Mésange', 4), ('Pic vert', 3), ('Pie', 2), ('Pinson', 1), ('Rouge-gorge', 2), ('Tourterelle', 4)]

def test_creer_ligne_sup():
    assert oiseaux.creer_ligne_sup(...)==...

def test_creer_ligne_noms_oiseaux():
    assert oiseaux.creer_ligne_noms_oiseaux(...)==...



