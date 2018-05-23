#atividade de lab 5.1
from math import sqrt

n = input()

lista = list(range(3, n+1, 2)) #gera a lista de inteiros impares ate n, imprime
primos = [2] #lista inicial dos primos
limco = int(sqrt(n)) #limite de corte
cont = 3#a contagem p a p sempre comeca em 3
noncort = lista[:]#numeros nao cortados a cada laco

print lista
print limco #imprime o limite superior de corte
    
while cont<= limco:
    inic=cont*cont
    cort = []#numeros cortados a cada laco

    print cont,inic,lista.index(inic)#contagem, p a p, valor incial da contagem, posicao na lista
        
    for x in range(lista.index(inic),len(lista),cont):
            cort.append(lista[x])  
            
            if lista[x] in noncort:#remove os cortados da lista de nao cortados
                noncort.remove(lista[x])
         
    print cort
    print noncort
     
    for x in noncort:
        if x > cont: 
            cont = x
            break

primos = primos + noncort
print sorted(primos)