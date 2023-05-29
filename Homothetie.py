''' Tracer l'image d'un polygone par homothétie'''
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

def homothetie(P1,J,lbda) :
    ''' reçoit un point P1, le centre J de l'homothétie et le rapport ldba
        retourne le point homothétique de P1 par l'homothétie de centre J 
        et de rapport lbda'''
        # fabrication du vecteur lbda * vec(J,P1)
    vec = Vector(J,P1,is_visible = False) # produit float*Vector impossible
    O = Point(0,0, is_visible = False)
    V = O + vec ; V.is_visible = False
    V_x = V.x * lbda
    V_y = V.y * lbda
    VV = Vector(V_x, V_y, is_visible = False)
    return J + VV


def homothetie_poly(Poly1,J, lbda):
    '''Reçoit la liste des sommets d'un polygone et les carctéristiques de l'homothétie
       Retoune la liste des sommets du polygône homothétique'''
    homo = []
    for P1 in Poly1 :
        PP1 = homothetie(P1,J, lbda) ; P1.color = "red" ; PP1.color = "violet"
        Segment(I,PP1, line_thickness = 1); time.sleep(1/2)
        homo.append(PP1)
    return homo
    #return [homthetie(P1,J, lbda) for P1 in Poly1]
    
I = Point(-5,-2, color = "blue")
lbda = 2
homothetique_figure1 = Polygon(homothetie_poly(liste_sommets_fig1,I, lbda), color = "violet")