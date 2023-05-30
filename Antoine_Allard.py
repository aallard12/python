#1.1
"""
terminaisons=['e','es','e','ons','ez','ent']
pronoms=['je','tu','il/elle','nous','vous','ils/elles']
voyelles=['a','e','i','o','u','y']

verbe=str(input("votre chaine ?"))
nouveauVerbe=""
for i in range(len(pronoms)):
    nouveauVerbe=verbe[:-2]+terminaisons[i]
    print("{0:11}{1:5}".format(pronoms[i],nouveauVerbe))
"""
#1.2
"""
terminaisons=['e','es','e','ons','ez','ent']
pronoms=['je','tu','il/elle','nous','vous','ils/elles']
voyelles=['a','e','i','o','u','y']

verbe=str(input("votre chaine ?"))
nouveauVerbe=""

for i in range(len(pronoms)):
    if verbe[:1]==voyelles[i]:
        pronoms[0]="j'"
    if verbe[-3]=="g":
        terminaisons[3]="eons"
    nouveauVerbe=verbe[:-2]+terminaisons[i]
    print("{0:11}{1:5}".format(pronoms[i],nouveauVerbe))
"""

#1.3
"""
terminaisons=['e','es','e','ons','ez','ent']
pronoms=['je','tu','il/elle','nous','vous','ils/elles']
voyelles=['a','e','i','o','u','y']

verbe=str(input("votre chaine ?"))
nouveauVerbe=""
for i in range(len(pronoms)):
    if verbe[:-2]=="er":
        if verbe[:1]==voyelles[i]:
            pronoms[0]="j'"
        if verbe[-3]=="g":
            terminaisons[3]="eons"
    else:
        print("Verbe non supporté")
    nouveauVerbe=verbe[:-2]+terminaisons[i]
    print("{0:11}{1:5}".format(pronoms[i],nouveauVerbe))
"""

#4.1
"""
liste=["bonjour","ici","fleur","fleuve","informatique"]
compteur=0
def motLePlusLong(liste):
    for n in range(len(liste)):

print(motLePlusLong(liste))
"""