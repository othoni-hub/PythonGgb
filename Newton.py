#import numpy as np

def f(t) :
    return t**3 - t - 1

xx = [x/100 for x in range(-200,400)]
yy = [f(x) for x in xx]

for t in xx :
    Point(t,f(t), size = 1)
    
x0 = 2
xxx = [x0]
yyy = [f(x0)]
iteration = 3

#Polynome(Point(xx[12], yy[12]), Point(xx[123], yy[123]), Point(xx[312], yy[312]), Point(xx[362], yy[362]))
    

def df(t): # dérivée
    return 3*t**2 - 1
    
def Newton(x0, iterations = iteration) :
    for _ in range(iterations) :
        x1 = -f(x0)/ df(x0) + x0
        P0 = Point(x0,f(x0), size = 2)
        P1 = Point(x1,0, size = 2)
        P2 = Point(x1,f(x1), size = 2)
        Segment(P0, P1 )
        Segment(P1, P2)
        x0 = x1
    return x1
    
x1 = Newton(x0)
print('Après ' + str(iteration) + ' itérations, une valeur approchée de la racine est : ' + str(x1))
print("L'ordonnée est alors : " + str(f(x1)))

    
    

    





