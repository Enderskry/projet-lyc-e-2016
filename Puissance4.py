# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:16:35 2016

@author: UYGUN Kaan
"""
# from constantesConsole import*
# from Listes import*
import os

#==============================================================================
#     Fichier Listes (vu que les import marchent pas)
#==============================================================================  

L1 = [0,0,0,0,0,0,0]
L2 = [0,0,0,0,0,0,0]
L3 = [0,0,0,0,0,0,0]
L4 = [0,0,0,0,0,0,0]
L5 = [0,0,0,0,0,0,0]
L6 = [0,0,0,0,0,0,0]

Grille = [L1, L2, L3, L4, L5, L6]

#==============================================================================
#     Fichier constantesConsole (vu que les import marchent pas)
#==============================================================================  

#Parametres de la fenetre
Erreur = 0
Colonne = 0
Joueur = 1
continuer = 1
PionsJoues = 0
P4 = 0
L = 0
PetiteChaine = ""
X = 1


while X:  #Boucle infinie
##=============================================================================
##                  Message de Bienvenue
##=============================================================================
    
    clear = lambda: os.system('cls')      
    print("Welcome")
    Jouer = input("Voulez-vous jouer ?\n")
    if Jouer == "oui" or Jouer == "Oui" or Jouer == "OUI":
        clear()
        Colonne = 0
        Joueur = 1
        continuer = 1
        PionsJoues = 0
        P4 = 0
        L = 0
        PetiteChaine = ""
        L1 = [0,0,0,0,0,0,0]
        L2 = [0,0,0,0,0,0,0]
        L3 = [0,0,0,0,0,0,0]
        L4 = [0,0,0,0,0,0,0]
        L5 = [0,0,0,0,0,0,0]
        L6 = [0,0,0,0,0,0,0]
        Grille = [L1, L2, L3, L4, L5, L6]
            
        while continuer:
#==============================================================================
#     Affichage grille
#==============================================================================                 
            clear()
            Col = 0 
            Lig = 0
            print(" | 0 | 1 | 2 | 3 | 4 | 5 | 6 |")
            print("  ___________________________")
            for Lig in  range(6):
                PetiteChaine = ""
                for Col in range(7):
                    if Grille[Lig][Col] == 0:
                        PetiteChaine = PetiteChaine + " | " + " "
                    else:
                        PetiteChaine = PetiteChaine + " | " + str(Grille[Lig][Col])
                    Col += 1
                print(PetiteChaine + " |")
                Lig += 1
            print("")
#==============================================================================
#     Vérification
#==============================================================================
            LongDiag = (Colonne+abs(L-5)) + 1
            N = 5 - (LongDiag - 1)
            
            loop = 0
            loop2 = 0
            loop3 = 0
            ChaineLigne = ""
            ChaineColonne = ""
            ChaineDiagonale1 = ""
            for loop in range (7):
                ChaineLigne = ChaineLigne + str(Grille[L][loop])
                loop += 1
            if 0 <= Colonne <= 6:
                for loop2 in range (6):
                    ChaineColonne = ChaineColonne + str(Grille[loop2][Colonne])
                    loop2 += 1
            if LongDiag<6:
                for loop3 in range (LongDiag):
                    ChaineDiagonale1 = ChaineDiagonale1 + str(Grille[N][loop3])
                    loop3 += 1
                    N += 1
            if ChaineDiagonale1.find("1111") != -1:
                P4 = 1
            elif ChaineDiagonale1.find("2222") != -1:
                P4 = 1
            elif ChaineColonne.find("1111") != -1:
                P4 = 1
            elif ChaineColonne.find("2222") != -1:
                P4 = 1
            elif ChaineLigne.find("1111") != -1:
                P4 = 1
            elif ChaineLigne.find("2222") != -1:
                P4 = 1
        
#==============================================================================
#     Fin vérification
#==============================================================================
            if P4 == 1:
                print ("Le joueur {} gagne la partie !".format(Joueur))
                break
            if PionsJoues == 42 and P4 == 0:
                print("Aucun joueur ne gagne la partie." )     
            if PionsJoues%2 == 0:
                Joueur = 1
            else:
                Joueur = 2
#==============================================================================
#     Position pion
#==============================================================================
            print("Joueur : ", Joueur)
            if Erreur == 0:
                print("")
            elif Erreur ==1:
                print("La colonne est remplie, veuillez choisir une autre colonne.")
            elif Erreur == 2:
                print("Veuillez entrer un nombre entre 0 et 6.")
            Colonne = int(input("Choisir la colonne a jouer : "))
            if 0 <= Colonne <= 6:
                L = 5
                while L>=0:
                    if Grille[L][Colonne] == 0:
                        Grille[L][Colonne] = Joueur
                        PionsJoues += 1
                        Erreur = 0
                        break
                    L-=1
                if L<0:
                    print("La colonne est remplie, veuillez choisir une autre colonne.")
                    Erreur = 1
            else:
                print("Veuillez entrer un nombre entre 0 et 6.")
                Erreur = 2

#==============================================================================
#     Fin position pion
#==============================================================================
    elif Jouer == "non" or Joueur == "Non" or Jouer == "NON":
            X = 0
            break
