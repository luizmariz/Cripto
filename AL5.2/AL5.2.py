#atividade de lab 5.2

k = input()
nac = [1] #lista de numeros altamente compostos >= n

def d(n): #funcao numero de divisores
    cont=0
    for number in range(1,n+1):
        if n%number == 0:
            cont+=1
    return cont

hcn_anterior = 1

for x in range(2,k+1):
   
    if d(x) > d(hcn_anterior):
        hcn_anterior = x
        nac.append(x)

print nac
