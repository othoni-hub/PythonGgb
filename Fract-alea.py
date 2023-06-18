# Dans un polygone, azimut aléatoire vers un sommet avec arrêt au milieu

from math import *
import random
import time

# Gébération du polygone
n = 3
R = 4
liste_points = [Point(R*cos(2*k*pi/n), R*sin(2*k*pi/n)) for k in range(n)]
Polygon(liste_points, color = "blue")

# milieu (non encore implémentée dans pythonGGB)
def milieu(P1, P2) :
    return Point((P1.x + P2.x)/2, (P1.y + P2.y)/2, size = 1, color = "blue")
    
#milieu(liste_points[0], liste_points[2])

# C'est parti : à chaque étape, on vise un sommet, 
# on se place au milieu entre ce sommet et le point courant
point_courant = liste_points[0]

for i in range(3000) :
    k = random.randint(0,n-1)
    sommet_vise = liste_points[k]
    point_courant = milieu(point_courant, sommet_vise)
    time.sleep(0.0001)
    
print("fini")
    


