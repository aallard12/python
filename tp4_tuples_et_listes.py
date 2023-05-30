"""
def afficheTuple(tuple):
    prenom, nom, adresse, codePostal, ville=tuple
    print("prénom : ",prenom)
    print("nom : ",nom)
    print("adresse : ",adresse)
    print("code postal : ", codePostal)
    print("ville : ",ville)
tuple=("bruce",'wayne','3 impasse de la chauve souris',72000,'le mans')
print(tuple)
"""

"""
def calcul(x,coefficientsDroite):
	a,b=coefficientsDroite
	y=a*x+b
	return y

coefficients=(2,1)
print("La valeur de y pour x=2 est: y=",calcul(2,coefficients))
"""

"""
from math import sqrt
def distance(ptA,ptB):
    xA,yA=ptA
    xB,yB=ptB
    AB=sqrt((xB-xA)*(xB-xA)+(yB-yA)*(yB-yA))
    return AB

pointA=(1,1)
pointB=(2,2)
print(distance(pointA,pointB))
"""

"""
def rechercheMin(list):
	min = list[0]
	for indice in range(1,len(list)):
		if list[indice] < min:
			min = list[indice]
	return min
list=[20,8,9,2,35,49]
print(rechercheMin(list))
"""

"""
def rechercheMax(liste):
    max = liste[0]
    for indice in range(1,len(liste)):
        if liste[indice] > max:
            max = liste[indice]
    return max
liste=[20,8,9,2,35,49]
print(rechercheMax(liste))
"""

"""
liste=[5,6,7,8,9,4]
somme=0
for n in range(len(liste)):
    somme=somme+liste[n]
print(somme)
"""

"""
def moyenneVersion1(liste):
    total=0
    for i in range(len(lst)):
        total=total+lst[i]
    moyenneVersion1=total/len(lst)
    return moyenneVersion1
lst=[20,8,9,2,39,45]
print(moyenneVersion1(lst))
"""

"""
def moyenneVersion2(liste):
    moy=sum(lst)/len(lst)
    return moy
lst=[20,8,9,2,39,45]
print(moyenneVersion2(lst))
"""

"""
def rechercheMoyenne(liste):
    moy=sum(lst)/len(lst)
    return moy

def rechercheMin(liste):
    min = lst[0]
    for indice in range(1,len(lst)):
        if lst[indice] < min:
            min = lst[indice]
    return min

def rechercheMax(liste):
    max = lst[0]
    for indice in range(1,len(lst)):
        if lst[indice] > max:
            max = lst[indice]
    return max
lst=[20,8,9,2,39,45]
print(rechercheMoyenne(lst))
print(rechercheMin(lst))
print(rechercheMax(lst))
"""