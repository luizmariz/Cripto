#atividade de laboratorio 12.3
def poten_mod(num,exp,mod):
         
    a = num
    b = exp
    c = mod

    A = a
    R = 1
    E = b


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
    
    return R

n = input()
for x in range(n):
    k = input()
    num_fermat = (2**(2**k))+1
    exp = (num_fermat-1)//2
    
    print num_fermat

    if poten_mod(5,exp,num_fermat) == num_fermat - 1:
        print "PRIMO"
        print "---"

    else:
        print "COMPOSTO"
        print "---"