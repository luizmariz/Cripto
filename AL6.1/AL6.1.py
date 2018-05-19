#atividade de lab 6.1
n = input()
for x in range(n):
    a,b,c = input() #onde c e o modulo
    
    forma_reduzida_a = a%c
    forma_reduzida_b = b%c
    soma_modulo = (a+b)%c 
    diferenca_modulo = (a-b)%c
    multiplicacao_modulo = (a*b)%c

    print forma_reduzida_a,forma_reduzida_b,soma_modulo,diferenca_modulo,multiplicacao_modulo,"\n---"