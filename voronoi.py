import random
import math

# initialisations
# map de couleurs
couleur_map = ["YELLOW","AQUA","SILVER","FUCHSIA" ,"GREEN","GRAY","BLUE" ,"LIME","MAROON","NAVY","OLIVE","PURPLE","TEAL"]

grain = 30 # finesse de la grille
num_points = 5 # nombre de points de la carte de Voronoi
bounds = [0, 8, 0, 8] # limites de la grille

def grille(bounds):
    # Crée une grille pour le diagramme de Voronoi
    xmin, xmax, ymin, ymax = bounds
    x = []
    y = []
    
    for k in range(grain+1) :
        x.append( xmin + k*(xmax-xmin)/grain )
        y.append( ymin + k*(ymax-ymin)/grain )
    
    grid = [[[x[j],y[k]] for j in range(grain+1)] for k in range(grain+1)]
    return(grid)

def dist(x1,y1,x2,y2) :
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
def generate_voronoi():
    # Calcul du point le plus proche pour chaque noeud de la grille
    for ligne in grid :
        for point_grille in ligne :
            distances = []
            min1 = 100
            k = 0
            for point in liste_points :
                d = dist(point_grille[0], point_grille[1], point.x, point.y)
                distances.append(d)
                if distances[k] < min1 :
                    min1 = distances[k]
                    rang_min1 = k # k est alors l'indice du point le plus proche
                # affectation de la couleur de la cellule du point k au point de la grille considéré
                Point(point_grille[0], point_grille[1], color = couleur_map[rang_min1 % num_points], size = 4)
                k = k+1

# Génère les points aléatoires dans les limites spécifiées
liste_points = []
for _ in range(num_points) :
    liste_points.append(Point(random.uniform(bounds[0],bounds[1]),random.uniform(bounds[2],bounds[3]), color = "red"))

grid = grille(bounds)
generate_voronoi()
