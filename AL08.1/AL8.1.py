#atividade de lab 8.1
n = input()
for x in range(n):
    b,a = input() #onde b eh o expoente e a ah base

    A = a
    R = 1
    E = b-1

    def impar(k): #funcao que ve se E eh impar 
        if (k%2 != 0):
            return True

    print R,A,E, "S" if impar(E) is True else "N" 

    while(E!=0):
        if(impar(E) is True):
            R = (R*A)%b
            E = (E-1)//2
            
        else:
            E = E//2
        
        A = (A*A)%b
        print R,A,E, "S" if impar(E) is True else "N"

    if R==1:
        print "INCONCLUSIVO" #pode ser primo ou pseudo primo
    else:
        print "COMPOSTO" #pelo pequeno teorema de fermat, com ctz eh composto
    
    print "---"