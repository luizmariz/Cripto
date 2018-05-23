#atividade de lab 7.2
n = input()
for x in range(n):
    a,b,c = input() #onde c e o modulo e e o expoente

    #pequeno teorema de fermat, se c e primo
    A = a
    R = 1
    E = b%(c-1)

    print E

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
    
    print "---"