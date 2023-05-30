NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)

def defilement(color):
    for p in range(NBPIXELS):
        np[p]=color
        np[(p-1)%NBPIXELS]=(255,0,0)
        np[(p+1)%NBPIXELS]=(255,0,0)
        np[(p+2)%NBPIXELS]=(0,0,255)
        np.write()
        sleep_ms(500)

while(True):
    defilement((0,0,255))