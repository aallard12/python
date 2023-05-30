"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def traceDroite(nbDroites,ecart):
    a=0
    for i in range(1,nbDroites+1):
        draw.line((a,0,a,255),fill=(0,255,0))
        a+=20
traceDroite(10,20)

#img.show()
"""

"""
from PIL import Image,ImageDraw,ImageFont
img=Image.new('RGB',(256,256),(0,0,0))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def cercle(x,y,rayon,couleur):
    draw.ellipse((x-rayon,y-rayon,x+rayon, y+rayon),fill=(couleur))

def tracecible(nbcercle):
    for i in range(1,nbcercle+1):
        cercle(125,125,90,(0,0,255))
        cercle(125,125,60,(255,0,0))
        cercle(125,125,30,(255,255,0))

tracecible(3)
img.save("effet.png")
"""

"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGB',(256,256),(255,255,255))
largeur,hauteur=img.size
draw=ImageDraw.Draw(img)

def rectangle(x,y,largeur,hauteur,couleur):
    draw.rectangle((x,y,x+largeur, y+hauteur),fill=couleur)

def traceEffetVisuel():
    rectangle(10,10,50,50(0,0,0))

traceEffetVisuel()
img.show()
"""

"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new("RGB",(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        img.putpixel((x,y),(0,0+x,0))
img.show()
"""

"""
from PIL import Image,ImageDraw,ImageFont

img=Image.new("RGB",(256,256),(0,0,0))
largeur,hauteur=img.size
for y in range(hauteur):
    for x in range(largeur):
        img.putpixel((x,y),(0+x,0+y,0+x))
img.show()
"""


from PIL import Image,ImageDraw,ImageFont

img=Image.new("RGB",(1536,256),(0,0,0))
largeur,hauteur=img.size

img.show()