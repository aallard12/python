#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    for i in range(len(notes)):
        somme+=notes[i]*coefficients[i]
    moyenne=somme/100
    print("Le nombre de points totals est de :",somme)
    return moyenne


def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<=8:
        print("Vous n'avez pas le bac !",moyenne)
    elif moyenne>8 and moyenne<=10:
        print("Vous allez en rattrapage !",moyenne)
    elif moyenne>10 and moyenne<=12:
        print("Vous avez votre bac !",moyenne)
    elif moyenne>12 and moyenne<=14:
        print("Vous avez une mention assez bien !",moyenne)
    elif moyenne>14 and moyenne<=16:
        print("Vous avez une mention bien !",moyenne)
    elif moyenne>16 and moyenne<=12:
        print("Vous avez une mention très bien !",moyenne)


def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(len(notes)):
        if notes[i]<min:
            min=notes[i]
    return min
print("Votre note la plus basse est de",rechercheNoteMin(notes))


def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(len(notes)):
        if notes[i]>max:
            max=notes[i]
    return max
print("Votre note la plus haute est de",rechercheNoteMax(notes))

def rechercheNote(notes,matieres,laNote):
    x=int(input("Cherchez une note ?"))
    compteur=0
    for i in range(len(notes)):
        if x==notes[i]:
            compteur+=1
            print("Vous avez obtenu",x,"dans",matieres[i])
    print("Vous avez obtenu",x,"dans",compteur,"matières")

"""
def changeNote(notes):
    for i in range(len(notes)):
        note=-1
        while (note<0 or note>20):
            print("Quel est votre note en",matieres[i])
            note=float(input())
        notes[i]=note
"""
def tableauBac(coefficients,notes,matieres):
    e="Enseignement"
    f="Coef"
    g="Notes"
    h="Résultat"
    print("{0:33}{1:11}{2:11}{3:11}".format(e,f,g,h))
    for i in range(len(notes)):
        a=matieres[i]
        b=coefficients[i]
        c=notes[i]
        d=notes[i]*coefficients[i]
        print("{0:33}{1:11}{2:11}{3:11}".format(a,b,c,d))


#changeNote(notes)
moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,12)
tableauBac(coefficients,notes,matieres)


#line_chart = pygal.HorizontalBar()
#line_chart.title = 'Notes du Bac (/20)'
#a completer question 8

#line_chart.render_to_file('notes.svg')

