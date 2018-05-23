#atividade de laboratorio 10.3
from math import sqrt

n = input()
for x in range(n):
    grupo, lista_subgrupo = input()
    
    numero = grupo    
    
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
        
    
    if fi%len(lista_subgrupo) != 0:
        print "NAO","\n---"

    else:

        
        ordem = grupo
        conjunto = []
        conjunto_teste = []

        for i in range(1,ordem+1):
            conjunto.append(i)
            conjunto_teste.append(i)

        for i in conjunto_teste:
        
            #inicio do AEE
            if i == 1:
                continue

            else:
                a = i
                b = ordem

            alpha1 = 1
            alpha2 = 0
            beta1 = 0
            beta2 = 1
    
            r=1

            while r > 0:
                r = a%b
                q = a//b
                alpha = alpha1-(alpha2*q)
                beta = beta1-(beta2*q)
        
                if r != 0:
                    
                    a = b
                    b = r
                    alpha1 = alpha2
                    alpha2 = alpha
                    beta1 = beta2
                    beta2 = beta
            
        
            if b != 1:
                conjunto.remove(i)
            else:
                if alpha2%ordem not in conjunto:
                    conjunto.remove(i)

            #fim do AEE 

        #Agora, vamos testar se lista_subgrupo eh subconjunto de U(n) e se o elemento neutro pertence ao subgrupo
        
        #teste 1

        if 1 not in lista_subgrupo:
            print "NAO","\n---" 
            continue

        ok = 0

        #teste 2

        for i in lista_subgrupo:
            if i not in conjunto:
                print "NAO","\n---"
                ok += 1 
                break

        #Agora, vamos testar se os termos do subgrupo * compoe ele mesmo
        
        #teste 3

        if ok != 0:
            continue
       
        for i in range(len(lista_subgrupo)):
            if ok != 0:
                break
            for j in range(len(lista_subgrupo)):
                
                produto = (lista_subgrupo[i])*(lista_subgrupo[j])
                
                if produto%ordem not in lista_subgrupo:
                    print "NAO","\n---" 
                    ok += 1
                    break

        #Agora, testaremos se todos os inversos dos termos do subgrupo estao no subgrupo

        #teste 4
        
        if ok != 0:
            continue
        
        for i in lista_subgrupo:
            
            #inicio do AEE
            if i == 1:
                continue

            else:
                a = i
                b = ordem

            alpha1 = 1
            alpha2 = 0
            beta1 = 0
            beta2 = 1
    
            r=1

            while r > 0:
                r = a%b
                q = a//b
                alpha = alpha1-(alpha2*q)
                beta = beta1-(beta2*q)
        
                if r != 0:
                    a = b
                    b = r
                    alpha1 = alpha2
                    alpha2 = alpha
                    beta1 = beta2
                    beta2 = beta
                
                    
            if b != 1:
                print "NAO","\n---" 
                ok += 1
                break
            else:
                if alpha2%ordem not in lista_subgrupo:
                    print "NAO","\n---" 
                    ok += 1
                    break

            #fim do AEE 

        if ok == 0:
            print "SIM","\n---"

