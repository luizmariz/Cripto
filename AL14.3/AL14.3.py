#atividade de laboratorio 14.3
from math import sqrt

n = input()
for x in range(n):
    g,h,p = input()

    m = int(sqrt(p-1)) + 1

    j = 0
    B = []
    
    print m

    while j<m:
        
        c = p
        R = 1
        A = g
        E = j

        def impar(x): #funcao que ve se E e impar 
            if (x%2 != 0):
                return True

        while(E!=0):
            if(impar(E) is True):
                R = (R*A)%c
                E = (E-1)//2
            
            else:
                E = E//2
        
            A = (A*A)%c
           
        s = R
        B.append(s)
        
        print j,s
        
        j += 1

    a = g
    b = p

    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1
 
    r=1

    while r > 0:
        r = a%b
        q = a//b
        x = x1-(x2*q)
        y = y1-(y2*q)
        
        if r != 0:
            
            a = b
            b = r
            x1 = x2
            x2 = x
            y1 = y2
            y2 = y


    c = p

    R = 1
    A = x2%p
    E = m

    while(E!=0):
        if(impar(E) is True):
            R = (R*A)%c
            E = (E-1)//2

        else:
            E = E//2
        
        A = (A*A)%c
        
    t = R
    i = 0

    while i<m:
        s = (h*(t**i))%p
        print i,s

        if s in B:
            pos = B.index(s)
            x = i*m + pos
            
            print i,pos
            print x
            break
        
        i += 1

    print "---"

            