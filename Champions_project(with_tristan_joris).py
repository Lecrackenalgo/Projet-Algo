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
    nb_joueur = int(input("Nombre de joueur(s) : "))
    while nb_joueur < 1 or nb_joueur > 2:
        print(f"Vous ne pouvez jouer qu'à 1 ou 2 joueurs")
        nb_joueur = int(input("Nombre de joueur(s) : "))
    return nb_joueur

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
            
afficher_grille(grille_jeu)

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
        
    

