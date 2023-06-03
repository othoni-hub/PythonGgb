import random as rd

N = 100000

frequences = [0]*19

for k in range(N): 
    de1 = rd.randint(1,6)
    de2 = rd.randint(1,6)
    de3 = rd.randint(1,6)
    somme = de1 + de2 + de3
    frequences[somme] = frequences[somme] + 1/N
    
frequences = [frequences[k]*100 for k in range(19)]
for k in range(19):
    Segment(Point(k,frequences[k]), Point(k,0, size = 1), color = "red")
#freq_9 = freq_9 * 100
#freq_10 = freq_10 * 100

#Segment(Point(9,freq_9), Point(9,0), color = "red")
#Segment(Point(10,freq_10), Point(10,0), color = "blue")
print('Fréquence du 9  : ' + str(frequences[9]))
print('Fréquence du 10 : ' + str(frequences[10]))
    
