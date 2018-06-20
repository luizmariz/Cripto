#atividade de laboratorio 13.2
from math import sqrt
n = input()
for x in range(n):
    num = input()

    num_mers = (2**num) - 1
    print num_mers

    r = int((sqrt(2**num))/(2*num))
    
    print r

    for x in range(1,r+1):
        q = 1 + 2*x*num
        print x
        c = q

        R = 1
        A = 2
        E = num

        def impar(x): #funcao que ve se E e impar 
            if (x%2 != 0):
                return True

        print R,A,E, "S" if impar(E) is True else "N" 

        while(E!=0):
            if(impar(E) is True):
                R = (R*A)%c
                E = (E-1)//2
            
            else:
                E = E//2
        
            A = (A*A)%c
            print R,A,E, "S" if impar(E) is True else "N"

        if R == 1: 
            print q, "\n---"
            break
            
    else:
        print num_mers,"\n---"
        