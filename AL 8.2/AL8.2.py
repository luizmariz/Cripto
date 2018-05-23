#atividade de lab 8.2
from math import sqrt

n = input()

for x in range(n):
    numero = input()
    cont = 0   
    numero_fixo = numero

    def teste(p,k):
        if k%(p*p)!=0 and (k-1)%(p-1) == 0:
            return 0
        else:
            return 1
    
    for y in range(2,int(sqrt(numero)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while numero%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            numero = numero//y
            
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            print y,expoente
            if teste(y,numero_fixo) == 1:
                cont+=1
   
    if numero != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        print numero,1
        cont+=1
         
    if cont==0:
        print "SIM" 
    else:      
        print "NAO"
    
    print "---"



