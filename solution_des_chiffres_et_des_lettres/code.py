# -*- coding: utf-8 -*-
# par : Kim Lavoie, Frederic Bolduc et Jules Minier
import random
import itertools
import time

# Clear l'écran
import os
os.system('cls' if os.name=='nt' else 'clear')

# on construit l'alphabet pour le tirage
consonnes = "bcdfghjklmnpqrstvwxz"
voyelles = "aeiouy"

# On accueillit notre participant
print("################################################")
print("# BIENVENUE A DES CHIFFRES ET DES LETTRES, WOO #")
print("################################################")
print("#                                              #")
print("#                       #####                  #")
print("#                       #    #                 #")
print("#                 #     #     #                #")
print("#                       #     #                #")
print("#                 #     #     #                #")
print("#                       #    #                 #")
print("#                       #####                  #")
print("#                                              #")
print("################################################")
print

# tirer 9 lettres
tirage = []
i, nombre_consonnes = 0, 0

while i < 9:
    choix = raw_input("Lettre " + str(i+1) + " de 9: Voyelle ou Consonne? (V ou C): ")

    #Si on choisit une consonne et qu'on peut encore
    if choix.strip().lower() == "c" and nombre_consonnes < 7:
        tirage.append(consonnes[random.randint(0,19)])
        nombre_consonnes+=1
        i+=1

    #Si on choisit une voyelle
    elif choix.strip().lower() == "v":
        tirage.append(voyelles[random.randint(0,5)])
        i+=1

    #Si on choisit une consonne, mais qu'on en a trop
    elif choix.strip().lower() == "c" and nombre_consonnes >= 7:
        print ("Vous ne pouvez pas avoir moins de 2 voyelles. Entrez une voyelle.")
    else:
        print ("Choix invalide")
        
    print "Tirage : [%s]\n" % (", ".join(tirage).upper())

tirage.append("-")

# on récupère le dictionnaire dans un dictionnaire (r\o/)
dictionnaire = {}
with open("Dictionnaire.txt") as f:
    for line in f:
        dictionnaire[line.strip()] = True

# on génère les beaucoup de possibilités de mots avec nos 9 lettres (puis 8, etc)
for n in xrange(9, 0, -1):      # for allant de 9 à 0 (exclue) avec un pas de -1
    solutions_possibles = []

    for combinaison in itertools.permutations(tirage, n):       # itertools.permutations(['a', 'b', 'c'], 3) vas générer toutes le permutations possibles de taille 3 avec les élement du tableau : ['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], etc.
        mot = "".join(combinaison)      # convertit le tableau combinaison en string. ex : "-".join(['a', 'b', 'c']) => "a-b-c"          "".join(['a', 'b', 'c']) => "abc"          " -> ".join(['a', 'b', 'c']) => "a -> b -> c"          

        if dictionnaire.get(mot):   # si le mot généré est dans le dico, on l'ajoute aux solutions
           solutions_possibles.append(mot.upper())

    if solutions_possibles: # si y'a des elements dans le tableau solutions_possibles
        print "\nSolutions possibles en %d lettres :" % n

        for solution in sorted(list(set(solutions_possibles))): # set() est une structure permetant de supprimer les doublon
            print solution

        print "\n################################################"
        print "############### YOU'RE WINNER !!! ##############"
        print "################################################\n"
        if os.name=='posix':
            os.system('say "wow such winner"')

        break
    
    else:
        print "Aucun mot trouvé en %d lettres" % n

# GREAT SUCCESS
