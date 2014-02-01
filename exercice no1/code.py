# -*- coding: utf-8 -*-
import random
import itertools

# on construit l'alphabet pour le tirage
consonnes = "bcdfghjklmnpqrstvwxz"
voyelles = "aeiouy"

# tirer 9 lettres
tirage = []
i = 0
nombre_consonnes = 0
while i < 9:
    choix = raw_input("Voyelle ou Consonne?(V ou C): ")

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
        
    

print "Tirage : %s" % (" ".join(tirage).upper())

#TODO FRED: test voir si ça règle les tirets
tirage.append("-")

# on récupère le dictionnaire dans un tableau
dictionnaire = {}
with open("Dictionnaire.txt") as f:
    for line in f:
        dictionnaire[line.strip()] = True

print ("Dico généré")

# on génère les baucoup possibilités de mots avec nos 9 lettres (puis 8, etc)
found = False
for n in xrange(9, 0, -1):
    solutions_possibles = []


    for combinaison in itertools.permutations(tirage, n):
        mot = "".join(combinaison)
        # si le mot géné ré est dans le dico on l'ajout aux solutions
        if dictionnaire.get(mot):
           solutions_possibles.append(mot.upper())

    if solutions_possibles:
        print "Solutions possibles en %d lettres :" % n
        solutions_possibles.sort()
        for solution in list(set(solutions_possibles)):
            print solution
        found = True
        break
    else:
        print "Aucun mot trouvé en %d lettres" % n

    if found:
        break


