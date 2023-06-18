# COURBE DU DRAGON RÉCURSIVE

# À partir d'un script Python, utilisant le module turtle, généré par ChatGPT, complètement fonctionnel (impressionnant !),
# transcription dans PythonGGB
# --> Les primitives de base de Turtle doivent être réécrites

from math import *
import time


def td(angle) : # angle en degrés
    global azimut
    azimut = azimut - angle 
    
def tg(angle) :
    global azimut
    azimut = azimut + angle 
    
def av(nb_pas) : # 1 pas = 1/100ème unité
    global x, y
    xx = x + nb_pas / 100 * cos(azimut * pi/180) # cos(angle en radians)
    yy = y + nb_pas / 100 * sin(azimut * pi/180) # sin(angle en radians)
    Segment(Point(x, y, is_visible = False), Point(xx, yy, is_visible = False), color = couleur, line_thickness = 1)
    x = xx
    y = yy
    time.sleep(0.001)
    
def gt(xx,yy): # déplacement sans trace
    global x, y
    x = xx
    y = yy

# initialisation
x = 0
y = 0
azimut = 90
# av(200) ; td(90) ; av(200) ; gt(2,3) ; tg(30) ; av(200)

def dragon_curve(order, length, angle, direction = 1):
    if order == 0:
        av(length)
    else:
        tg(direction * angle / 2)
        dragon_curve(order-1, length, angle, 1)
        tg(direction * angle)
        dragon_curve(order-1, length, angle, -1)
        tg(direction * angle / 2)
# 1er dragon        
couleur = "red"        
dragon_curve(10, 10, 90)

# 2ème dragon imbriqué dans le premier
couleur = "blue"
gt(0,0)
dragon_curve(10, 10, 90, -1)

print("fini")


    


