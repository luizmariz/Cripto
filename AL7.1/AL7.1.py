#atividade de lab 7.1
n = input()

for i in range(n):
    num,mod = input() #onde a modulo b
    
    a = num
    b = mod
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1

    print a,"-",x1,y1,"\n",b,"-",x2,y2
    
    r=1
    #inicio do AEE
    while r > 0:
        r = a%b
        q = a//b
        x = x1-(x2*q)
        y = y1-(y2*q)
        
        if r != 0:
            print r,q,x,y
            mdc = r
            alpha = x
            a = b
            b = r
            x1 = x2
            x2 = x
            y1 = y2
            y2 = y
            
        else:
            print r,q,"-","-"

    if mdc != 1:  
        print 0
    
    if mdc == 1:
        mod_alpha = alpha%mod
        print mod_alpha


    print "---"