'''Construction entièrement à la règle et au compas
d'un pentagone régulier dont le rayon est régi par un curseur'''

import time

r = Slider(1, 5, increment=0.1)

# repère
O = Point(0,0, size = 2)

vecti = Vector(r,0)
vectj = Vector(0,r) 
ax_x = Line(O, O + vecti)
ax_y = Line(O ,O + vectj)

#1er bâti
C01 = Circle(O,r, color = "red"); time.sleep(1/2)

A = Intersect(C01,ax_x,2)
Z = Intersect(C01,ax_x,1); Z.size = 1
J = Intersect(C01,ax_y,2); J.size = 1

# médiatrice de [OZ] et placement de I, milieu 
C02 = Circle(J,r, color = "yellow"); time.sleep(1/2)
U = Intersect(C02,C01,1); U.size = 1
V = Intersect(C02,C01,2); V.size = 1
d0 = Line(U,V, color = "yellow"); time.sleep(1/2)
I = Intersect(d0,ax_y,1); I.size = 1

# construction du pentagone
d1 = Line(Z,I); time.sleep(1/2)

R = r.value # inutile

C2 = Circle(I,O, color = "blue"); time.sleep(1/2)



M = Intersect(d1,C2,1); M.size = 3
N = Intersect(d1,C2,2); N.size = 3

C3 = Circle(Z,M, color = "violet"); time.sleep(1/2)

C4 = Circle(Z,N, color = "orange"); time.sleep(1/2)

B = Intersect(C4,C01,1); time.sleep(1/2)
E = Intersect(C4,C01,2); time.sleep(1/2)
C = Intersect(C3,C01,1); time.sleep(1/2)
D = Intersect(C3,C01,2); time.sleep(1/2)

Liste_sommets = [A,B,C,D,E]

pentag = Polygon(Liste_sommets)