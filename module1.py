#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 08:07:58 2022

@author: tverdet
"""
def verif_gagne(bj):
    """
    La liste en paramètre est la liste qui contient nos variables bateaux_i.
    Retourne un booléen qui vaut True si un des joueurs a gagné sinon retourne False.
    """
    s = 0
    for x in bj:
        s += x
    if s == 0:
        res = True
    else:
        res = False
    return res


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
                coords = def_coordonnees(coord)
                if grille_j[coords[0]][coords[1]] == '.':
                    res = True
                else:
                    prirnt("Vous avez déjà tiré dans cette case. Sah vise mieux !")
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

def afficher_grille(grille_jeu):
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
    for ligne in grille_jeu:
        print("\n")
        for case in ligne:
            print(case, end="")
            
def verif_placmnt_bateaux(c1, c2, n, grille_pos):
    """Fonction qui vérifie si les 2 coordonnées sont bien sur la même ligne ou même colonne, on ne peut
    pas placer de bateaux en diagonale.
    On ne peut pas non plus placer un bateau sur un bateau deja placé.
    c1 et c2 sont des coordonnées sous la forme [i,j] ou i est l'indice de la ligne et j l'indice de la colonne pour notre liste 2D. 
    n est la taille du bateau considéré.
    """
    if c1[0] == c2[0] : #On est bien horizontal
        if abs(c1[0]-c2[0]) == n:
            i = c1[1]
            while not grille_pos[c1[0]][i]: #On vérifie qu'il n'y a pas de bateau entre les 2 points extrêmes
                i += 1
            if i != c2[1]: #On est pas arrivé à la dernière coordonnées donc il y a un bateau 
                res = False
                print("Impossible de placer un bateau ici car il y a un autre bateau entre les coordoonées que vous avez saisies")
            else:
                res = True
        else:
            print(f"Le bateau que vous essayez de placer à une taille de {n} or la distance entre les 2 coordonnées que vous avez saisie \
            est de {abs(c1[0]-c2[0])}")
            res = False
    else: #On est vertical
        i = c1[0]
        while not grille_pos[i][c1[0]] :
            i += 1
        if abs(c1[0]-c2[0]) == n:
            if i != c2[0] :
                print("Impossible de placer un bateau ici car il y a un autre bateau entre les coordoonées que vous avez saisies")
                res = False
            else:
                res = True
        else:
            print(f"Le bateau que vous essayez de placer à une taille de {n} or la distance entre les 2 coordonnées que vous avez saisie \
            est de {abs(c1[1]-c2[1])}")
            res = False
    return res
        
    def placement_bateaux(n, l1):
    
    """
    Permet au joueur de placer ses bateaux de taillesentre 2 et 5 dans
    l'arène verticalement ou horizontalement (en modifiant les valeurs 
    de la liste contenant l'arène)
    """
    #premiere coordonnée
    a = int(input("coordonnées colonne"))
    b = int(input("coordonnée ligne"))
    
    vertical = bool(input("vertical ou horizontale"))
    
    if (vertical):
        
        for i in range(a,a+n):
            l1[a][i] = True
    else:
        
        for i in range(b,b+n):
            l1[i][b] = True
        
        
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
