#atividade de laboratorio 13.1
from math import sqrt
def poten_mod(num,exp,mod):
         
    a = num
    b = exp
    c = mod

    A = a
    R = 1
    E = b


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
    
    return R


m = input()
for x in range(m):
    n = input()
    #estabelecendo as condicoes

    def condic1(b,n):
        e = n-1
        print e
        if poten_mod(b,e,n) == 1:
            return 1
        else:
            return 0
    
    def condic2(b,n,p):
        e = (n-1)//p
        print e
        if poten_mod(b,e,n) != 1:
            return 1
        else:
            return 0

    lista_fator = []
    lista_expoente = []
    ordem = n-1

    #algoritmo ingenuo de fatoracao

    for y in range(2,int(sqrt(ordem)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while ordem%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            ordem = ordem//y
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            print y,expoente
            lista_fator.append(y)
            lista_expoente.append(expoente)

   
    if ordem != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        print ordem,1 
        lista_fator.append(ordem)
        lista_expoente.append(1)  

    
   
    lista_aux = lista_fator[:]

    for y in range(2,n):
        
        base = y
        print base


        if condic1(base,n) == 0:
            print "COMPOSTO"
            print "---" 
            break
        else:
            for p in lista_aux:
                if p == -1:
                    continue
                
                if condic2(base,n,p) == 1:  
                    lista_aux[lista_aux.index(p)] = -1
                    
                if all(i == -1 for i in lista_aux):
                    print "PRIMO","\n---"
                    break
            else:
                continue
            
            break

    if any(i != -1 for i in lista_aux): #se ao menos um fator for diferente de -1
        print "COMPOSTO","---"
