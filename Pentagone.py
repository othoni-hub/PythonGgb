
#R = Slider(1, 5, increment=0.1)
import time

R = 4
O = Point(0,0, size = 1)
J = Point(0,R, size = 1)
K = Point(-R,0, size = 1)
A = Point(R,0)

#I = Point(0,R.value/2, size = 1)
I = Point(0,R/2, size = 1)
C1 = Circle(O,R, color = "violet")
time.sleep(1/2)

#C2 = Circle(I,R.value/2, color = "blue")
C2 = Circle(I,R/2, color = "blue")
time.sleep(1/2)

d1 = Line(K,I)
time.sleep(1/2)

M = Intersect(d1,C2,1)
M.size = 1
N = Intersect(d1,C2,2)
N.size = 1

C3 = Circle(K,M, color = "green")
time.sleep(1/2)

C4 = Circle(K,N, color = "green")
time.sleep(1/2)

B = Intersect(C4,C1,1)
time.sleep(1/2)
E = Intersect(C4,C1,2)
time.sleep(1/2)
C = Intersect(C3,C1,1)
time.sleep(1/2)
D = Intersect(C3,C1,2)
time.sleep(1/2)

Liste_sommets = [A,B,C,D,E]

pentag = Polygon(Liste_sommets)
