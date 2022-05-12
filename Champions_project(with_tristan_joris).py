# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:13:43 2022

@author: joris
"""

def nombre_joueurs():
    """
    Permet au(x) joueur(s) de sélectionner le nombre de participants à la partie
    Ce nombre ne peut-être que 1 ou 2 sinon message d'erreur
    """
    nb_joueur = input("Nombre de joueur(s) : ")
    while ord(nb_joueur)<49 or ord(nb_joueur)>50: 
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
    while  ord(nb_bat)<50 or ord(nb_bat)>54 or len(nb_bat) != 1:
        print("Vous devez rentrer un nombre compris entre 2 et 6")
        nb_bat = input("Combien de bateaux par joueur ? (2-6) :  ")
    for loop in range(int(nb_bat)):
        taille_bateau = input(f"Quelle taille pour le bateau numéro {loop+1} (entre 2 et 5) :  ")
        while ord(taille_bateau)<50 or ord(taille_bateau)>53 or len(taille_bateau) != 1 :
            print("Veuillez rentrer un nombre compris entre 2 et 5")
            taille_bateau = input(f"Quelle taille pour le bateau numéro {loop+1} (entre 2 et 5) :  ")
        bateaux.append(int(taille_bateau))
    return (bateaux, bateaux)
    
def verif_placmnt_bateaux(c1, c2, n, grille_pos):
	"""Fonction qui vérifie si les 2 coordonnées sont bien sur la même ligne ou même colonne, on ne peut
	pas placer de bateaux en diagonale.
	On ne peut pas non plus placer un bateau sur un bateau deja placé.
	c1 et c2 sont des coordonnées sous la forme [i,j] ou i est l'indice de la ligne et j l'indice de la colonne pour notre liste 2D. 
	n est la taille du bateau considéré.
	"""
	if c2[0] > 10 or c2[1] > 10 :
		print("Vous essayez de placer un bateau trop près du bord.")
		res = False # Il n'y a pas la place pour faire rentrer un bateau 
	else:
		if c1[0] == c2[0] :#On est horizontal
			i = c1[0]
			while i < c2[0] and not grille_pos[c1[0]][i] :
				i += 1
			if i != c2[0] :
				print("Vous essayez de placer un bateau trop proche d'un autre bateau.")
				res = False
			else:
				res = True
		else: #Normalement on est forcément vertical
			i = c1[1]
			while i < c2[1] and not grille_pos[i][c1[1]] :
				i += 1 
			if i != c2[1] :
				print("Vous essayez de placer un bateau trop proche d'un autre bateau.")
				res = False
			else:
				res = True
		return res
			
        
def placement_bateaux(n, grille_pos):
		"""
		Permet au joueur de placer ses bateaux de tailles entre 2 et 5 dans
		l'arène verticalement ou horizontalement (en modifiant les valeurs 
		de la liste contenant l'arène)
		"""
		#premiere coordonnée
		a = input("coordonnée ligne entre 1 et 10 :  ")
		while len(a) != 1 or ord(a)<47 or ord(a)> 58:
			print("Rentrez un chiffre entre 1 et 10 !")
			a = input("coordonnée ligne entre 1 et 10 :  ")
		a = int(a)
		b = (input("coordonnées colonne entre A et H :  "))
		while len(b) != 1 or ord(b)<65 or ord(b)> 72 :
			print("Rentrez une lettre majuscule entre A et H")
		print(a,b)
		b = ord(b) - 64
		c1 = [a,b] #Coordonnée du bateau en indices
		vertical = input("vertical ou horizontal (tapez h ou v) :  ")
		while vertical not in "hv" or len(vertical) != 1 :
			vertical = input("vertical ou horizontal (tapez h ou v) :  ")
		if vertical == "v":
			vertical = True
		else:
			vertical = False

		if vertical:
			c2  = [a+n, b] #Coordonées du bateau en indice
			print(a+n, chr(b+64))
			if verif_placmnt_bateaux(c1, c2, n, grille_pos):
				for i in range(a,a+n):
					grille_pos[a][i] = True
			else:
				placement_bateaux(n, grille_pos)
		else:
			c2 = [a, b+n]#Coordonées du bateau en indice
			print(a, chr(b+n+64))
			if verif_placmnt_bateaux(c1, c2, n, grille_pos):
				for i in range(b,a+n):
					grille_pos[i][b] = True 
			else:
				placement_bateaux(n, grille_pos)
		print(c2)
		#afficher_grille(grille_pos)

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
    print("\n")

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
bateaux_1, bateaux_2 = init_bateau()
print("bateaux:  ", bateaux_1, bateaux_2)
somme_1 = sum(bateaux_1)
somme_2 = sum(bateaux_2)
grille_jeu_1 = grille_jeu()
#aff_grille_jeu_1 = afficher_grille(grille_jeu_1)
grille_jeu_2 = grille_jeu()
aff_grille_jeu_2 = afficher_grille(grille_jeu_2)

#PROGRAMME :

nombre_joueurs = 2 #nombre_joueurs()

grille_position_1 = grille_pos(11,False)    #Initialisation des grilles de position
grille_position_2 = grille_pos(11,False)    #Initialisation des grilles de position

if nombre_joueurs == 2:
    #Placement des bateaux joueur 1 (pas tès optimisé)
    for x in bateaux_1:
        placement_bateaux(x, grille_position_1)
    for x in bateaux_2:
        placement_bateaux(x, grille_position_2)
    while somme_1 != 0 or somme != 0:
        print(f"C'est au tour de joueur 1")
        aff_grille_jeu_1 = afficher_grille(grille_jeu_1)
        coordonnees_tir = def_coordonnees()
        while not verif_coord(coordonnees_tir,grille_jeu_1):
            coordonnees_tir = def_coordonnees()
        trad_coord = trad_coordonnees(coordonnees_tir)
        bateau_touche(trad_coord,grille_position_1,grille_jeu_1,5,somme_1,"joueur 1")
