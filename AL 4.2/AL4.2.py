#atividade de lab 4.2
from math import sqrt
n = input()

for x in range(n):
    numero = input()
    x = int (sqrt(numero))
    y = 0 
    
    while numero != ((x**2) - (y**2)):
        print x,y,"N"
        x+=1
        y = int (sqrt((x**2)-numero))
    
    print x,y,"S","\n",(x-y),(x+y),"\n---"
        