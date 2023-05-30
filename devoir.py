
#EX 2

"""
from random import randint
def plus_ou_moins():
    nb_mystere = randint(1, 100)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0
    while nb_mystere != nb_test and compteur < 11:
        compteur += 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))
    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)
plus_ou_moins()
"""

#EX 1

"""
def renverse(mot):
    nouveauMot=" "
    for i in range(len(mot)):
        nouveauMot+=mot[-i-1]
    return nouveauMot

print(renverse("informatique"))
"""

#EX 3

"""
def recherche(lettre,mot):
    nb_occurences=0
    for i in range(len(mot)):
        if lettre==mot[i]:
            nb_occurences+=1
    return nb_occurences

print(recherche('e', "sciences")) #2
print(recherche('i', "mississippi")) #4
print(recherche('a', "mississippi"))#0
"""

#EX 4
def correspond(mot,mot_a_trous):
    for i in range(len(mot_a_trous)):
        if len(mot)!=len(mot_a_trous):
            return False
        else:
            return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE')) #True
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE')) #False
print(correspond('STOP', 'S*')) #False
print(correspond('AUTO', '*UT*')) #True