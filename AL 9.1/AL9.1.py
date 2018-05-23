#atividade de lab 9.1

n = input()
for x in range(n):
    lista_congru,lista_mod = input()
    
    for y in range(len(lista_mod)):
        #inicio do AEE
        if y == 1:
            continue
        if y == 0:
            mn = lista_mod[0]*lista_mod[1]
            a = lista_mod[0]
            b = lista_mod[1]

        else:
            a = mn
            b = lista_mod[y]
            ma = mn
            mb = lista_mod[y]
        
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

        if y == 0:
            congru = ((lista_congru[0]*lista_mod[1]*beta2)+(lista_congru[1]*lista_mod[0]*alpha2))%mn 
            
        else:
            mn = mn*mb
            congru = ((congru*mb*beta2)+(lista_congru[y]*ma*alpha2))%mn

        print congru,mn
   
    print "---"