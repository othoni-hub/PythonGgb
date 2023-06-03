''' Tracer un pavage à partir d'un quadrilatère quelconque
    Groupe des symtries-translations'''
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

def milieu(P1,P2) : # pas encore de Middle en PythonGgb
    '''Cette fonction reçoit deux points et renvoie le point milieu'''
    return Point((P1.x + P2.x)/2,(P1.y + P2.y)/2)
    
I = milieu(A,B) ; I.color = "green"; I.size = 2
J = milieu(B,C) ; J.color = "green"; J.size = 2
K = milieu(C,D) ; K.color = "green"; K.size = 2
L = milieu(A,D) ; L.color = "green"; L.size = 2

V1 = Vector(A,C)
V2 = Vector(B,D)

def translation(P1,v) :
    ''' reçoit un point P1 et un vecteur v
        retourne le point translaté de P1 par la translation de vecteur v'''
    return P1 + v

def translation_poly(Poly1,v):
    '''Reçoit la liste des sommets d'un polygone et le vecteur de translation
       Retoune la liste des sommets du polygône translaté'''
    trans = []
    for P1 in Poly1 :
        PP1 = translation(P1,v) ; P1.color = "red" ; PP1.color = "violet"
        Segment(P1,PP1, line_thickness = 1); time.sleep(1/2)
        trans.append(PP1)
    return trans
    #return [translation(P1,v) for P1 in Poly1]
    
def symetrie_centrale(P1,J) :
    ''' reçoit un point P1 et le centre de symétrie J
        retourne le point symétrique de P1 par rapport à J'''
    v = Vector(P1,J, is_visible = False)
    return J + v

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
    
liste_sommets_fig2 = translation_poly(liste_sommets_fig1,V1)
figure2 = Polygon(liste_sommets_fig2, color = "orange")

liste_sommets_fig3 = symetrie_centrale_poly(liste_sommets_fig1,L)
figure3 = Polygon(liste_sommets_fig3, color = "violet")

liste_sommets_fig4 = translation_poly(liste_sommets_fig3,V1)
figure4 = Polygon(liste_sommets_fig4, color = "violet")

liste_sommets_fig5 = translation_poly(liste_sommets_fig1,V2)
figure5 = Polygon(liste_sommets_fig5, color = "orange")

liste_sommets_fig6 = translation_poly(liste_sommets_fig5,V1)
figure6 = Polygon(liste_sommets_fig6, color = "orange")

# composition
liste_sommets_fig7 = symetrie_centrale_poly(translation_poly(liste_sommets_fig5,V1),J)
figure7 = Polygon(liste_sommets_fig7, color = "black")

# faire deux boucles, avec poly courant, poly image
# avec transfert de liste élt par élt

