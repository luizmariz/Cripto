#Atividade de laboratorio 12.1
from math import sqrt
n = input()
for x in range(n):
    numero = input()#calculo da ordem do grupo do numero primo    
    p = numero
    fi = 1

    for y in range(2,int(sqrt(numero)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while numero%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            numero = numero//y
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            fi = fi*((y**(expoente-1))*(y-1))
      
    if numero != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        expoente = 1
        
        fi = fi*((numero**(expoente-1))*(numero-1))
        ordem = fi
        
    
    ordem = fi  
    lista_fator = []
    lista_expoente = []
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
    
    
    #inic do algoritmo de gauss
    

    def poten_mod(num,exp,mod):
         
        a = num
        b = exp
        c = mod

        #pequeno teorema de fermat, se c e primo
        A = a
        R = 1
        E = b%(c-1)


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

        return R
            

    k = len(lista_fator)
    i = 1
    g = 1

    #gauss
    
    while i<= k: 
        a = 2
        e = (p-1)//(lista_fator[i-1])

        while poten_mod(a,e,p) == 1:
            a += 1
        
        e2 = (p-1)//(lista_fator[i-1]**lista_expoente[i-1])
        h = poten_mod(a,e2,p)

        print lista_fator[i-1],a,h

        g = (g*h)%p
        i += 1

    print g
    print "---"