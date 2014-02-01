# -*- coding: utf-8 -*-
import random
import itertools

# on construit l'alphabet pour le tirage
alpha = "abcdefghijklmnopqrstuvwxyz"

# tirer 9 lettres
tirage = []
for i in xrange(0, 9):
    tirage.append(alpha[random.randint(0,25)])

#tirage = ['j', 'u', 'l', 'e', 's'] # tirage de test à (de)commenter plus tard

print "Tirage : %s" % (" ".join(tirage).upper())

# on récupère le dictionnaire dans un tableau
dictionnaire = []
with open("Dictionnaire.txt") as f:
    for line in f:
        dictionnaire.append(line.strip())

# dico de test à (de)commenter plus tard
#dictionnaire = ['jules', 'ulesj', 'elusj', 'banane', 'moncul']

# on génère les baucoup possibilités de mots avec nos 9 lettres (puis 8, etc)
for n in xrange(9, 0, -1):
    solutions_possibles = []


    for combinaison in itertools.permutations(tirage, n):
        mot = "".join(combinaison)
        if mot in dictionnaire: # si le mot géné ré est dans le dico on l'ajout aux solutions
           solutions_possibles.append(mot.upper())

    if solutions_possibles:
        print "Solutions possibles en %d lettres :" % n
        solutions_possibles.sort()
        for solution in solutions_possibles:
            print solution
    else:
        print "Aucun mot trouvé en %d lettres" % n

