#atividade de lab 4.1
from math import sqrt

n = input()
for x in range(n):
    numero = input()    
    
    for y in range(2,int(sqrt(numero)+1)):#existe algum fator em 2<= y <= raizdonumero
        expoente = 0  
        
        while numero%y == 0: #enquanto o numero puder ser dividido por um fator ele sera
            expoente+=1
            numero = numero//y
        
        if expoente != 0: #caso sim, numero nao e primo,como qlqr coisa^0=1, descartamos    
            print y,expoente
   
    if numero != 1: #o algoritmo sempre acaba em 1, caso nao: numero e primo
        print numero,1     
           
    print "---"
        
        
        
            
        



