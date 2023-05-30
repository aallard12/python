#Simulateur deux dés
from random import*
caisse=100
prix_partie=30
x=random(randint(0,10))
y=random(randint(0,10))
result=x+y
while caisse>=prix_partie:
    if result>=18 and result<=4:
        caisse=caisse-prix_partie
        caisse=caisse+100
        print(result)
        print("Vous venez de gagner 50€")
        print("Votre caisse est de :",caisse)

    elif result<=17 and result>=5:
        caisse=caisse-prix_partie
        caisse=caisse+10
        print(result)
        print("Vous venez de gagner 10€")
        print("Votre caisse est de :",caisse)