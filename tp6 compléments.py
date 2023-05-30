"""
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=' ' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille


texte=str(input("votre texte ?"))
print(affichagebaille(texte))
"""

"""
def insertionTexte(texte):
    nouveauTexte=''
    for i in range(len(texte)-1):
        nouveauTexte+=texte[i]+"*"
    nouveauTexte=nouveauTexte+texte[-1]
    return nouveauTexte
texte=str(input("Votre texte ?"))
print(insertionTexte(texte))
"""

"""
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(chaine,total)
"""

"""
chaine=str(input("chaine"))
total=""
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]
print(chaine,total)
if chaine==total:
    print("Bien joué !")
else:
    print("Mauvais")
"""

"""
def codecesar(phrase,cle):
    total=""
    for i in range(0,len(phrase)):
        ascii=ord(phrase[i])
        conv=ascii-65+cle
        caract=chr(conv+65)
        total+=caract+""
    return total
cle=int(input("clef"))
phrase=str(input("phrase"))
print(codecesar(phrase,cle))
"""

"""
from string import ascii_uppercase as ascUp
vigenereTable=[ascUp[i:]+ascUp[:i]for i in range(len(ascUp))]
for ligne in range(0,len(vigenereTable)):
    print(vigenereTable[ligne])

total=""
cle=str(input("clef"))
phrase=str(input("phrase"))
for i in range(0,len(phrase)):
    ascii=ord(phrase[i])
    conv=ascii-65+cle[i]
    caract=chr(conv+65)
print(phrase,cle)
"""