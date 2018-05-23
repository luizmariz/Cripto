#atividade de laboratorio 10.1
n = input()
for x in range(n):
    ordem = input()
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
       
    print conjunto,"\n---"
