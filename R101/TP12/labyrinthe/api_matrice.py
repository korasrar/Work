import random
import csv

import random
import csv

def creer_matrice(nombre_lignes, nombre_colonnes,valeurdefaut=0):
    matrice = []
    for _ in range(nombre_lignes):
        ligne_matrice = []
        for _ in range(nombre_colonnes):
            ligne_matrice.append(valeurdefaut)
        matrice.append(ligne_matrice)
    return matrice

def get_valeur(matrice, ligne, colonne):
    return matrice[ligne][colonne]

def set_valeur(matrice, ligne, colonne, valeur):
    matrice[ligne][colonne] = valeur

def get_ligne(matrice, num_ligne):
    return matrice[num_ligne]

def get_colonne(matrice, num_colonne):
    return [matrice[i][num_colonne] for i in range(len(matrice))]

def get_nombre_de_colonnes(matrice):
    return len(matrice[0]) if matrice else 0

def get_nombre_de_lignes(matrice):
    return len(matrice)

def enregistre_matrice(matrice, nom_fichier):
    with open(nom_fichier, 'w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        for ligne in matrice:
            writer.writerow(ligne)

def charge_matrice(nom_fichier):
    matrice_chargee = []
    with open(nom_fichier, 'r') as fichier_csv:
        reader = csv.reader(fichier_csv)
        for ligne in reader:
            ligne_entiers = [int(valeur) for valeur in ligne]
            matrice_chargee.append(ligne_entiers)
    return matrice_chargee

def affiche_ligne_separatrice(matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nombre_de_colonnes(matrice) + 1):
        print('-' * taille_cellule + '+', end = '')
    print()


def affiche(matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nombre_de_colonnes(matrice)
    nb_lignes = get_nombre_de_lignes(matrice)
    print(' '*taille_cellule+'|', end='')
    for indice in range(nb_colonnes):
        print(str(indice).center(taille_cellule) + '|', end = '')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for ind in range(nb_lignes):
        print(str(ind).rjust(taille_cellule) + '|', end = '')
        for ind_j in range(nb_colonnes):
            print(str(get_val(matrice, ind, ind_j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()
