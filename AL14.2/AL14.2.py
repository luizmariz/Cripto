#atividade de laboratorio 14.2

n = input()
for x in range(n):
    primo,chave,s,t = input()
    
    c = primo
    R = 1
    A = s
    E = primo - 1 - chave 

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
    
    print (R*t)%primo
    print "---"