def f(t) :
    return t**3 - t - 1

pas = 100
xx = [x/pas for x in range(-2*pas,4*pas)]
yy = [f(x) for x in xx]

for t in xx :
    Point(t,f(t), size = 1)
    
#val_x0 = Slider(1, 3, increment=0.1)
#x0 = val_x0.value*2.2

x0 = 2
PP0 = Point(x0, f(x0))
xxx = [x0]
yyy = [f(x0)]
iteration = 3

def df(t): # dérivée
    return 3*t**2 - 1


def Newton(x0, iterations = iteration) :
    for _ in range(iterations) :
        x1 = -f(x0)/ df(x0) + x0
        P0 = Point(x0,f(x0), size = 2)
        P1 = Point(x1,0, size = 2)
        P2 = Point(x1,f(x1), size = 2)#P2 = Point(x1,f(x1), size = 2,is_visible=False)
        Segment(P0, P1)
        Segment(P1, P2)
        x0 = x1
    return x1
    
x1 = Newton(x0)
print('Après ' + str(iteration) + ' itérations, une valeur approchée de la racine est : ' + str(x1))
print("L'ordonnée est alors : " + str(f(x1)))

    
    

    



