#Travaux Pratiques 2 Boucles

"""
for n in range(1,16,1):
    print(n)
"""

"""
for n in range(15,-1,-1):
    print(n)
"""
"""
x=int(input("Votre valeur du début : "))
y=int(input("Votre valeur de fin : "))
for n in range(x,y,1):
    print(n)
"""

"""
x=int(input("Votre valeur de début : "))
for n in range(x+1,x+10,1):
    print(n)
"""

"""
x=int(input("Votre table de multiplication : "))
for n in range(1,11):
    print(x*n)
"""

"""
max=0
for n in range(5):
    nb=int(input("Saisir un nombre : "))
    if nb>max:
       max=nb
print("Le nombre max est",max)
"""

"""
valeur=0
max=0
while valeur>=0:
    valeur=int(input("Saisir un nombre positif : "))
    if valeur>max:
       max=valeur
print("Le nombre max est",max)
"""

"""
valeur=0
somme=0
while valeur>=0:
      valeur=int(input("Saisir un nombre positif : "))
      somme=somme+valeur
print("La somme des nombres est : ",somme)
"""

"""
menu=0
while menu!="q":
      print("1 : Charger le fichier")
      print("2 : Sauvegarder le fichier")
      print("3 : Afficher les données")
      print("4 : Modifier les données")
      print("q : Quitter")
      print("Votre choix ?")
      menu=input("Tapez votre choix : ")
      if menu=='1':
         print("Chargement...")
      elif menu=='2':
            print("Sauvegarde...")
      elif menu=='3':
           print("Affichage...")
      elif menu=='4':
           print("Modification...")
      elif menu=='q':
           print("Vous venez de quitter le menu !")
      else:
           print("Erreur 404")
"""

"""
from random import*
x=randint(1,100)
print(x)
"""

"""
from random import randint
nombre=randint(1,20)
valeur=0
while valeur != nombre:
    valeur=int(input("Votre chiffre : "))
    if valeur > nombre :
        print("Chiffre trop grand")
    elif valeur < nombre:
        print("Chiffre trop petit")
    else:
        print("exact")
"""


from random import randint
x=randint(1,20)
y=0
coups=0
while y!=x :
    y=int(input("Votre chiffre : "))
    if y>x :
        print("Chiffre trop grand !")
        coups=coups+1
    elif y<x :
        print("Chiffre trop petit !")
        coups=coups+1
    else:
        print("Exact ! Vous venez de gagner à mon jeu !")
        coups=coups+1
print("Votre nombre de coups : ",coups)




