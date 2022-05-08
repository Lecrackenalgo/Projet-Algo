#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 09:27:05 2022

@author: jdorsemain
"""

def nombre_joueurs():
    """
    Permet au(x) joueur(s) de sélectionner le nombre de participants à la partie
    Ce nombre ne peut-être que 1 ou 2 sinon message d'erreur
    """
    nb_joueur = input("Nombre de joueur(s) : ")
    while nb_joueur < 1 or nb_joueur > 2 or ord(nb_joueur)<47 or ord(nb_joueur)>58: 
        print(f"Vous ne pouvez jouer qu'à 1 ou 2 joueurs et n'oubliez pas de rentrer un nombre !")
        nb_joueur = input("Nombre de joueur(s) : ")
    return int(nb_joueur)

def init_bateau():
    """
    Permet au(x) joueur(s) de sélectionner le nombre de bateaux et leurs taille avec lesquels ils jouent.
    Ces nombres ne peuvent être qu'entre 2 et 6 sinon message d'erreur.
    Retourne une liste de la forme [taille_bateau1, taille_bateau2, taille_bateau3, ...]
    """
    bateaux = []
    nb_bat = input("Combien de bateaux par joueur ? (2-6) :  ")
    while  ord(nb_joueur)<47 or ord(nb_joueur)>58:
        print("Vous devez rentrer un nombre! ")
        nb_bat = input("Combien de bateaux par joueur ? (2-6) :  ")
    for loop in range(int(nb_bat)):
        taille_bateau = input(f"Quelle taille pour le bateau numéro {loop} (entre 2 et 5) :  ")
    
    

def grille_pos(n,e):
    """
    génère une grille de n lignes et n colonnes
    e est l'élément contenu dans chaque cellule
    """
    grille = [list()]*n
    for k in range(len(grille)):
        grille[k] = [e]*n
    return grille

def grille_jeu():
    l1 = []
    l2 = ["   ", "A","B", "C", "D", "E", "F", "G", "H", "I", "J"]
    l1.append(l2)
    for y in range(1,11):
        l1.append([f"{y}  ",".",".",".",".",".",".",".",".",".","."])
    return(l1)

#grille_jeu = grille_jeu()

def afficher_grille(grille):
    """
    On veut une grille de la forme:
     ABCDEFGHIJ
    1..........
    2..X.......
    3.......O..
    4.......O..
    5...X......
    6..........
    7.....OOO..
    8..........
    9.....X....
   10..........
  
   Le paramètre grille est une liste 2D. On part du principe que la liste est déjà sous la bonne forme.
    """
    for ligne in grille:
        print("\n")
        for case in ligne:
            print(f"{case:4}", end="")

def def_coordonnees():
    """
    Renseignement des coordonnees sous forme de chaîne de caractères
    """
    coordonnees = input("Renseignez vos coordonnées de tir : ")
    return coordonnees

def trad_coordonnees(coordonnees):
    """
    Convertit des coordonnées sous forme de chaîne de caractère donnés en paramètre en liste
    """
    nouvelles_coordonnees = []
    nouvelles_coordonnees.append(int(coordonnees[1])) #Position sur les lignes
    nouvelles_coordonnees.append(ord(coordonnees[0]) - 64) #Position sur les colonnes
    return nouvelles_coordonnees

def verif_coord(coord, grille_j):
    """
    Le paramètre coord correspond à la saisie de l'utilisateur qui doit être sous la forme A5 par exemple c'est à dire
    'colonne ligne'. Avec la lettre de la colonne en majuscules
    grille_j est la liste qui stocke tout les tirs déja effectués.
    Cette fonction retourne un booléen correspondant à la validité des coordonnées.
    """
    ex = "Un exemple de coordonnée valide serait :F2"
    if len(coord) <= 3:
        try:
            ligne = int(coord[1:])
        except ValueError:
            print("La coordonnée correspondant à la ligne doit être un chiffre\n", ex)
            res = False
        if ligne <= 10 and ligne > 0:
            if ord(coord[0]) >= 65 and ord(coord[0])<= 74:
                coords = def_coordonnees()
                print(coords)
                if grille_j[coords[0]][coords[1]] == '.':
                    res = True
                else:
                    print("Vous avez déjà tiré dans cette case. Sah vise mieux !")
                    res = False
            else:
                print("La coordonnée correspondant à la colonne doit être en majuscule entre A et J (inclus).\n", ex)
                res = False
        else:
            print("Vous avez rentré un numéro de ligne qui ne rentre pas dans le tableau.\n", ex)
            res = False
    else:
        print("Vous avez rentré des coordonnées trop longues !\n", ex)
        res = False
    return res

def bateau_touche(coord, grille_pos, grille_jeu,nv_vie,somme,joueur):
    """
    Cherche si les coordonnées renseignées en paramètre correspondent à la position d'un bâteau
    Si un bateau est touché, indiqué la touche sur la grille de jeu, réduire de 1 la vie du bâteau et la somme
    """
    if grille_pos[coord[0]][coord[1]]:  #Bateau touché
        grille_jeu[coord[0]][coord[1]] = "X"
        aff_grille_jeu = afficher_grille(grille_jeu)
        nv_vie -= 1
        somme -= 1
        if nv_vie == 0:
            print("Touché, coulé !")
        else:
            print("Touché !")
        print(f"{joueur} joue à nouveau")
    else:   #Tir dans l'eau
         grille_jeu[coord[0]][coord[1]] = "O"
         aff_grille_jeu = afficher_grille(grille_jeu)
         print("Plouf, c'est raté")
         print(f"C'est au tour de l'adversaire")
         

         
#afficher_grille(grille_jeu)

#Définition des variables :
somme_1 = 17
somme_2 = 17
grille_jeu_1 = grille_jeu()
aff_grille_jeu_1 = afficher_grille(grille_jeu_1)
grille_jeu_2 = grille_jeu()
aff_grille_jeu_2 = afficher_grille(grille_jeu_2)

#PROGRAMME :

nombre_joueurs = nombre_joueurs()

grille_position_1 = grille_pos(11,False)    #Initialisation des grilles de position
grille_position_2 = grille_pos(11,False)    #Initialisation des grilles de position

if nombre_joueurs == 2:
    #Placement des bateaux
    while somme_1 != 0 or somme != 0:
        print(f"C'est au tour de joueur 1")
        aff_grille_jeu_1 = afficher_grille(grille_jeu_1)
        coordonnees_tir = def_coordonnees()
        while not verif_coord(coordonnees_tir,grille_jeu_1):
            coordonnees_tir = def_coordonnees()
        trad_coord = trad_coordonnees(coordonnees_tir)
        bateau_touche(trad_coord,grille_position_1,grille_jeu_1,5,somme_1,"joueur 1")
    
