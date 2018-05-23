#atividade de lab 8.3

n = input()
for x in range(n):
    def impar(x): #funcao que ve se E e impar 
        if (x%2 != 0):
            return True
        else:
            return False
    
    numero,base = input()
    
    k = 0 
    q = numero -1

    while impar(q) is False:#acha a forma num = 2 elevado a k vezes q
        k+=1
        q = q/2

    print k,q #1 

    R = 1
    A = base
    E = q

    print R,A,E, "S" if impar(E) is True else "N" 
    while(E!=0):
        if impar(E) is True:
            R = (R*A)%numero
            E = (E-1)//2
            
        else:
            E = E//2
        
        A = (A*A)%numero
        print R,A,E, "S" if impar(E) is True else "N"

    print q,R
    t = R

    if t==1 or t==n-1:
        print "INCONCLUSIVO"
        print "---" 
        continue

    else:
        aux = 1
        aux2 = q
        while aux<k:
            aux2 = 2*aux2
            t=(t*t)%numero
            print aux2,t
            if t == numero -1:
                print "INCONCLUSIVO" 
                break
            aux+=1
    
    if t != numero -1:
        print "COMPOSTO"       
    print "---"    