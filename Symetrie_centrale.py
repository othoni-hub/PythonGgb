''' Tracer l'image d'un polygone par symétrie centrale'''
# SAMR :    A : Augmentation fonctionnelle par rapport à Python seul (facilité graphique)
#               Point Ggb en tant que variable Python
#           M : look in the box (par rapport à l'usage d'un bouton Ggb) :
#               conceptualiser textuellement la transformation géométrique
#           R : Concevoir la transformation géométrique comme une action sur les figures
#               (impossible dans Ggb)

import time

# Figure initiale
A = Point(-1,-1)
B = Point(-2,0)
C = Point(0,2)
D = Point(2,1)
# Les points sont mobiles dans le cadre Ggb et la figure totalement dynamique

liste_sommets_fig1 = [A,B,C,D]
figure1 = Polygon(liste_sommets_fig1)

def symetrie_centrale(P1,J) :
    ''' reçoit un point P1 et le centre de symétrie J
        retourne le point symétrique de P1 par rapport à J'''
    v = Vector(P1,J, is_visible = False)
    return J + v


I = Point(2,2)

def symetrie_centrale_poly(Poly1,J):
    '''Reçoit la liste des sommets d'un polygone et le centre de symétrie J
       Retoune la liste des sommets du polygône symétrique par rapport à J'''
    sym = []
    for P1 in Poly1 :
        PP1 = symetrie_centrale(P1,J) ; P1.color = "red" ; PP1.color = "violet"
        Segment(P1,PP1, line_thickness = 1); time.sleep(1/2)
        sym.append(PP1)
    return sym
    #return [symetrie_centrale(P1,J) for P1 in Poly1]
    
symetrique_figure1 = Polygon(symetrie_centrale_poly(liste_sommets_fig1,I))