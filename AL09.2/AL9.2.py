#atividade de lab 9.2
from math import sqrt
n = input()
for x in range(n):
    base,e,mod = input() 
    lista_congru = []   
    lista_mod = []
    
    #inicio do algoritmo de fatoracao ingenua

    for y in range(2,int(sqrt(mod)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while mod%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            mod = mod//y
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            print y,expoente
            lista_mod.append(y)
   
    if mod != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        print mod,1     
    
    #fim da fatoracao ingenua
    #inicio do mini teorema de fermat

    a = base
    b = e 

    for z in range(len(lista_mod)):
        c = lista_mod[z]
        if a%c == 0:
            print 0
            lista_congru.append(0)
        else:
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
            lista_congru.append(R)

    #fim do mini fermat
    #inicio do algoritmo chines do resto
    
    for p in range(len(lista_mod)):
        
        #inicio do AEE
        if p == 1:
            continue
        if p == 0:
            mn = lista_mod[0]*lista_mod[1]
            a = lista_mod[0]
            b = lista_mod[1]

        else:
            a = mn
            b = lista_mod[p]
            ma = mn
            mb = lista_mod[p]
        
        alpha1 = 1
        alpha2 = 0
        beta1 = 0
        beta2 = 1

        print a,"-",alpha1,beta1,"\n",b,"-",alpha2,beta2
    
        r=1

        while r > 0:
            r = a%b
            q = a//b
            alpha = alpha1-(alpha2*q)
            beta = beta1-(beta2*q)
        
            if r != 0:
                print r,q,alpha,beta
                a = b
                b = r
                alpha1 = alpha2
                alpha2 = alpha
                beta1 = beta2
                beta2 = beta
            else:
                print r,q,"-","-","\n",alpha2,beta2
        
        #fim do AEE

        if p == 0:
            congru = ((lista_congru[0]*lista_mod[1]*beta2)+(lista_congru[1]*lista_mod[0]*alpha2))%mn 
            
        else:
            mn = mn*mb
            congru = ((congru*mb*beta2)+(lista_congru[p]*ma*alpha2))%mn

        print congru,mn
   
    print "---"