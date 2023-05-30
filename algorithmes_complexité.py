from pylab import *

def calcul_nb_pliages(hauteur):
    epaisseur_feuille=0.0001
    somme_hauteur=epaisseur_feuille
    pliages=0
    while somme_hauteur<hauteur:
        somme_hauteur=somme_hauteur*2
        print(somme_hauteur)
        pliages+=1
        x.append(somme_hauteur)
        y.append(pliages)
    print(somme_hauteur)
    return pliages
x=[]
y=[]
print(calcul_nb_pliages(1.6))