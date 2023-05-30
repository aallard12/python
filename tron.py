"""
Programme du tron
nom(s), prénom(s), classe(s)
"""
import pygame
from random import randint

#constantes de la fenêtre d'affichage
LARGEUR=384       #hauteur de la fenètre
HAUTEUR=384       #largeur de la fenètre
ROUGE=(219,23,2)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,191,255)
ORANGE=(255,128,0)
x1=randint(0,76)
x2=randint(0,76)
x3=randint(77,152)
x4=randint(77,152)
x5=randint(153,228)
x6=randint(153,228)
x7=randint(229,304)
x8=randint(229,304)
x9=randint(305,380)
x10=randint(305,380)
x11=randint(0,76)
x12=randint(229,304)
x13=randint(77,152)
x14=randint(153,228)
x15=randint(153,228)
x16=randint(77,152)
x17=randint(229,304)
x18=randint(0,76)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Tron")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
motoX=LARGEUR//3
motoY=HAUTEUR//2
direction = 'haut'
direction2 = 'haut'
tempsPartie=0

def dessineDecor():
    """
    dessine un decor
    """
    pygame.draw.rect(fenetre, ROUGE, [1, 1, LARGEUR-1, HAUTEUR-1],1)
    #pygame.draw.circle(fenetre, ROUGE, (x,y), 10)      #cercle plein aux coord x,y de rayon 10
    #pygame.draw.rect(fenetre, BLEU, [x, y, 10, 10],0)  #rectangle plein aux coord x,y

def afficheRectangle(x,y,largeur,hauteur):
    pygame.draw.rect(fenetre, ROUGE, [x1, x2, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x3, x4, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x5, x6, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x7, x8, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x9, x10, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x11, x12, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x13, x14, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x15, x16, largeur, hauteur])
    pygame.draw.rect(fenetre, ROUGE, [x17, x18, largeur, hauteur])

def afficheTexte(x,y,txt):
    """
    affiche un texte aux coordonnées x,y
    """
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))

def collisionMur(x,y):
    """
    verifie si on touche un mur ou autre chose
    aucun obstacle correspond à  une couleur noire
    """
    color=fenetre.get_at((x, y))[:3]
    somme=color[0]+color[1]+color[2]
    if somme==0:
        collision=False
    else:
        collision=True
    return collision

def deplacementmoto():
    """
    deplace la moto si c'est possible
    """
    global motoX,motoY
    touche=False
    if direction=='haut':
        x=motoX
        y=motoY-1
        touche=collisionMur(x,y)
    elif direction=='bas':
        x=motoX
        y=motoY+1
        touche=collisionMur(x,y)
    elif direction=='droite':
        x=motoX+1
        y=motoY
        touche=collisionMur(x,y)
    elif direction=='gauche':
        x=motoX-1
        y=motoY
        touche=collisionMur(x,y)
    if touche==False:       #si pas d'obstacle alors on trace le point de la moto
        motoX=x
        motoY=y
    fenetre.set_at((x, y), BLEU)
    return touche           #retourne la variable booleenne touche pour savoir si la partie est terminée

loop=True
dessineDecor()
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenètre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE: #touche échap pour quitter
                loop = False
            #fenetre.set_at((200, 200), color)

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:
        direction = 'haut'
    elif keys[pygame.K_DOWN]:
        direction = 'bas'
    elif keys[pygame.K_RIGHT]:
        direction = 'droite'
    elif keys[pygame.K_LEFT]:
        direction = 'gauche'
    elif keys[pygame.K_z]:
        direction2 = 'haut'
    elif keys[pygame.K_s]:
        direction2 = 'bas'
    elif keys[pygame.K_d]:
        direction2 = 'droite'
    elif keys[pygame.K_q]:
        direction2 = 'gauche'

    #fenetre.fill((0,0,0))   #efface la fenêtre, non utilisée ici

    if deplacementmoto()==True:
        loop=False
    print(afficheRectangle(x1,x2,20,20))
    print(afficheRectangle(x3,x4,20,20))
    print(afficheRectangle(x5,x6,20,20))
    print(afficheRectangle(x7,x8,20,20))
    print(afficheRectangle(x9,x10,20,20))
    print(afficheRectangle(x11,x12,20,20))
    print(afficheRectangle(x13,x14,20,20))
    print(afficheRectangle(x15,x16,20,20))
    print(afficheRectangle(x17,x18,20,20))
    frequence.tick(80)
    pygame.display.update() #mets à  jour la fenêtre graphique
    tempsPartie+=1
pygame.quit()
print('perdu')
print('temps partie',tempsPartie)