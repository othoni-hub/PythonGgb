''' Tracer l'image d'un polygone par translation'''
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
figure1 = Polygon(liste_sommets_fig1, color = "red")

def translation(P1,v) :
    ''' reçoit un point P1 et un vecteur v
        retourne le point translaté de P1 par la translation de vecteur v'''
    return P1 + v


def translation_poly(Poly1,J):
    '''Reçoit la liste des sommets d'un polygone et le vecteur de translation
       Retoune la liste des sommets du polygône translaté'''
    trans = []
    for P1 in Poly1 :
        PP1 = translation(P1,v) ; P1.color = "red" ; PP1.color = "violet"
        Segment(P1,PP1, line_thickness = 1); time.sleep(1/2)
        trans.append(PP1)
    return trans
    #return [translation(P1,v) for P1 in Poly1]
    
v = Vector(A,D, color = "blue")
    
translatee_figure1 = Polygon(translation_poly(liste_sommets_fig1,v), color = "violet")