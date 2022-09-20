# Créé par antoine.allard, le 20/09/2022 en Python 3.7
from random import*
caisse=100
nb_partie=30
x=random(randint(0,10))
y=random(randint(0,10))
result=x+y
caisse=caisse-nb_partie
while caisse>=nb_partie:
    if result>=18 and result<=4:
        caisse=caisse+100
        print(result)
        print("Vous venez de gagner 100€")
        print("Votre caisse :",caisse)
