# fichier de tests de la SAE 1.01 partie 1
# bilan carbone d'activités mystères en septembre 2024

# on importe toutes les fonctions et données définies dans le fichier bilan_carbone
# l'appel de ces fonctions et données doit être préfixé par bc. 
import bilan_carbone as bc  

# ---------------------------------------------------------------------------------------------
# Exemples de tests à compléter impérativement
# ---------------------------------------------------------------------------------------------

def test_est_avant():
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4')) == True
    assert bc.est_avant(('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-01', 67.2, 'type3')) == False
    assert bc.est_avant(('Marx', '2024-09-01', 80.3, 'type1'), ('korasrar', '2024-09-01', 67.2, 'type1')) == True
    assert bc.est_avant(('korasrar', '2024-09-01', 67.2, 'type2'), ('Marx', '2024-09-01', 45.3, 'type3')) == True

def test_annee():
    assert bc.annee(('Lucas', '2024-09-01', 67.2, 'type3')) == '2024'
    assert bc.annee(('Lucas', '1999-12-27', 70.08, 'type3')) == '1999'
    assert bc.annee(('Marx', '17-09-01', 67.2, 'type1')) == '17'
    assert bc.annee(('korasrar', '0-12-27', 70.08, 'type4')) == '0'

def test_annee_mois():
    assert bc.annee_mois(('Lucas', '2024-10-01', 67.2, 'type3')) == '2024-10'
    assert bc.annee_mois(('Lucas', '2023-09-01', 67.2, 'type3')) == '2023-09'
    assert bc.annee_mois(('Marx', '17-09-01', 67.2, 'type3')) == '17-09'
    assert bc.annee_mois(('korasrar', '0-12-27', 67.2, 'type3')) == '0-12'

def test_max_emmission():
    assert bc.max_emmission([]) == None
    assert bc.max_emmission(bc.liste1) == ('David', '2024-09-29', 23, 'type4')
    assert bc.max_emmission(bc.liste4) == ('David', '2024-09-27', 21, 'type2')
    assert bc.max_emmission(bc.liste5) == ('Erika', '2024-09-28', 240.5, 'type2')

def test_filtre_par_prenom():
    assert bc.filtre_par_prenom([], 'Lucas') == []
    assert bc.filtre_par_prenom([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')], 'Lucas') == [('Lucas', '2024-09-01', 67.2, 'type3')]
    assert bc.filtre_par_prenom(bc.liste1, 'David') == [('David', '2024-09-26', 18, 'type1'), ('David', '2024-09-27', 21, 'type2'), ('David', '2024-09-28', 17, 'type3'), ('David', '2024-09-29', 23, 'type4')]
    assert bc.filtre_par_prenom(bc.liste4, 'Marx') == []
    assert bc.filtre_par_prenom(bc.liste5, 'Erika') == [('Erika', '2024-09-01', 34.8, 'type1'), ('Erika', '2024-09-02', 20.01, 'type1'), ('Erika', '2024-09-03', 26.1, 'type1'), ('Erika', '2024-09-04', 17.4, 'type1'), ('Erika', '2024-09-05', 20.88, 'type1'), ('Erika', '2024-09-06', 30.45, 'type1'), ('Erika', '2024-09-07', 53.07, 'type1'), ('Erika', '2024-09-08', 65.25, 'type1'), ('Erika', '2024-09-09', 6.96, 'type1'), ('Erika', '2024-09-10', 28.71, 'type1'), ('Erika', '2024-09-11', 28.71, 'type1'), ('Erika', '2024-09-12', 5.22, 'type1'), ('Erika', '2024-09-13', 18.27, 'type1'), ('Erika', '2024-09-14', 36.54, 'type1'), ('Erika', '2024-09-15', 17.4, 'type1'), ('Erika', '2024-09-16', 20.01, 'type1'), ('Erika', '2024-09-17', 26.1, 'type1'), ('Erika', '2024-09-18', 52.2, 'type1'), ('Erika', '2024-09-19', 33.93, 'type1'), ('Erika', '2024-09-20', 29.58, 'type1'), ('Erika', '2024-09-21', 57.42, 'type1'), ('Erika', '2024-09-22', 62.64, 'type1'), ('Erika', '2024-09-23', 50.46, 'type1'), ('Erika', '2024-09-24', 18.27, 'type1'), ('Erika', '2024-09-25', 6.96, 'type1'), ('Erika', '2024-09-26', 17.4, 'type1'), ('Erika', '2024-09-27', 4.35, 'type1'), ('Erika', '2024-09-28', 76.56, 'type1'), ('Erika', '2024-09-29', 39.15, 'type1'), ('Erika', '2024-09-30', 55.68, 'type1'), ('Erika', '2024-09-01', 110.5, 'type2'), ('Erika', '2024-09-02', 63.05, 'type2'), ('Erika', '2024-09-03', 81.9, 'type2'), ('Erika', '2024-09-04', 54.6, 'type2'), ('Erika', '2024-09-05', 67.6, 'type2'), ('Erika', '2024-09-06', 95.55, 'type2'), ('Erika', '2024-09-07', 165.75, 'type2'), ('Erika', '2024-09-08', 204.1, 'type2'), ('Erika', '2024-09-09', 22.1, 'type2'), ('Erika', '2024-09-10', 89.7, 'type2'), ('Erika', '2024-09-11', 90.35, 'type2'), ('Erika', '2024-09-12', 16.9, 'type2'), ('Erika', '2024-09-13', 59.15, 'type2'), ('Erika', '2024-09-14', 114.4, 'type2'), ('Erika', '2024-09-15', 54.6, 'type2'), ('Erika', '2024-09-16', 64.35, 'type2'), ('Erika', '2024-09-17', 82.55, 'type2'), ('Erika', '2024-09-18', 162.5, 'type2'), ('Erika', '2024-09-19', 107.9, 'type2'), ('Erika', '2024-09-20', 94.25, 'type2'), ('Erika', '2024-09-21', 180.05, 'type2'), ('Erika', '2024-09-22', 195.65, 'type2'), ('Erika', '2024-09-23', 158.6, 'type2'), ('Erika', '2024-09-24', 58.5, 'type2'), ('Erika', '2024-09-25', 22.1, 'type2'), ('Erika', '2024-09-26', 55.25, 'type2'), ('Erika', '2024-09-27', 14.95, 'type2'), ('Erika', '2024-09-28', 240.5, 'type2'), ('Erika', '2024-09-29', 122.85, 'type2'), ('Erika', '2024-09-30', 175.5, 'type2')]

def test_filtre():
    assert bc.filtre([], 3, 'type1') == []
    assert bc.filtre(bc.liste3, 1, '2024-09-29') == [('David', '2024-09-29', 23, 'type4'), ('Guillaume', '2024-09-29', 22, 'type4')]
    assert bc.filtre(bc.liste3, 1, 'type6') == []
    assert bc.filtre(bc.liste3, 6, 'type3') == []

def test_cumul_emmissions():
    assert bc.cumul_emmissions([]) == 0
    assert bc.cumul_emmissions(bc.liste4) == 78
    assert bc.cumul_emmissions(bc.liste3) == 144
    assert bc.cumul_emmissions(bc.liste5) == 33710.84000000004

def test_plus_longue_periode_emmissions_decroissantes():
    assert bc.plus_longue_periode_emmissions_decroissantes([]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste6) == 3
    assert bc.plus_longue_periode_emmissions_decroissantes([('Marx', '2024-09-01', 89, 'type1'), ('korasrar', '2024-09-02', 89, 'type1')]) == 0
    assert bc.plus_longue_periode_emmissions_decroissantes(bc.liste5) == 4

def test_est_bien_triee():
    assert bc.est_bien_triee([]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == True
    assert bc.est_bien_triee([('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type3')]) == False

def test_liste_des_types():
    assert bc.liste_des_types([]) == []
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type3']
    assert bc.liste_des_types([('Lucas', '2024-09-01', 67.2, 'type4'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['type4', 'type3']

def test_liste_des_personnes():
    assert bc.liste_des_personnes([]) == []
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ['Lucas']
    assert bc.liste_des_personnes([('Lucas', '2024-09-01', 67.2, 'type3'), ('David', '2024-09-02', 70.08, 'type3')]) == ['Lucas', 'David']
    assert bc.liste_des_personnes(bc.liste6) == ['Erika']

def test_fusionner_activites():
    assert bc.fusionner_activites([], []) == []
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3')], [('Lucas', '2024-09-02', 70.08, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-01', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]
    assert bc.fusionner_activites([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], [('Lucas', '2024-09-03', 67.2, 'type3')]) == [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3'), ('Lucas', '2024-09-03', 67.2, 'type3')]
    assert bc.fusionner_activites(bc.liste3, bc.liste4) == bc.liste2
def test_premiere_apparition_type():
    assert bc.premiere_apparition_type([], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3')], 'type1') == None
    assert bc.premiere_apparition_type([('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')], 'type3') == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste5, 'type1') == '2024-09-01'
    assert bc.premiere_apparition_type(bc.liste3, 'type3') == '2024-09-28'

def test_recherche_activite_dichotomique():
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', []) == None
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', [('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-02', 70.08, 'type3')]) == ('Lucas', '2024-09-01', 67.2, 'type3')
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', bc.liste5) == ('Lucas', '2024-09-01', 26.88, 'type3')
    assert bc.recherche_activite_dichotomique('Lucas', '2024-09-01', 'type3', bc.liste1) == None

def test_charger_sauver():
    ...

def test_temps_activite():
    assert bc.temps_activite(('Lucas', '2024-09-01', 67.2, 'type3'), bc.co2_minute) == 67.2/0.96
    assert bc.temps_activite(('Lucas', '2024-09-02', 70.08, 'type5'), bc.co2_minute) is None
    assert bc.temps_activite(('Marx', '2024-09-01', 34.87, 'type1'), bc.co2_minute) == 34.87/0.87
    assert bc.temps_activite(('korasrar', '2024-09-01', 75.34, 'type2'), bc.co2_minute) == 75.34/0.65

def test_cumul_temps_activite():
    assert bc.cumul_temps_activite([], bc.co2_minute) == 0
    assert bc.cumul_temps_activite([('Lucas', '2024-09-01', 67.2, 'type3')], bc.co2_minute) == 67.2/0.96
    assert bc.cumul_temps_activite(bc.liste4, bc.co2_minute) == 113.97414845690707
    assert bc.cumul_temps_activite(bc.liste5, bc.co2_minute) == 43734.0
# ---------------------------------------------------------------------------------------------
# Ajoutez ici les tests manquants (vos propres fonctions le cas échéant)
# ---------------------------------------------------------------------------------------------

