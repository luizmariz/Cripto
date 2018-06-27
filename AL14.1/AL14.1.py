#atividade de laboratorio 14.1
from math import sqrt

i = input()
for x in range(i):
    n,e,bloco = input()

    #algoritmo de fatoracao de fermat

    x = int (sqrt(n))
    y = 0 
    
    while n != ((x**2) - (y**2)):
        print x,y,"N"
        x+=1
        y = int (sqrt((x**2)-n))
    
    fator_1 = x - y
    fator_2 = x + y

    print x,y,"S","\n",fator_1,fator_2

    #achando fi de n

    fi = 1
    numero = n

    for y in range(2,int(sqrt(numero)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while numero%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            numero = numero//y
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            fi = fi*((y**(expoente-1))*(y-1))
             
    nao_precisa = 0 
    if numero != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        expoente = 1
        fi = fi*((numero**(expoente-1))*(numero-1))
        print fi
        nao_precisa += 1
    
    if nao_precisa == 0:
        print fi
    
    #aplicando o AEE

    a = e
    b = fi

    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1

    print a,"-",x1,y1,"\n",b,"-",x2,y2
    
    r=1

    while r > 0:
        r = a%b
        q = a//b
        x = x1-(x2*q)
        y = y1-(y2*q)
        
        if r != 0:
            print r,q,x,y
            a = b
            b = r
            x1 = x2
            x2 = x
            y1 = y2
            y2 = y
        else:
            print r,q,"-","-"
        
    d = x2%fi
    print d

    #decodificando o bloco

    c = n
    R = 1
    A = bloco
    E = d

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

    print R
    
    print "---"
        
