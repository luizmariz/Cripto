#atividade de lab 3.1

n = input()

for i in range(n):
    a,b = input()
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1

    print a,"-",x1,y1,"\n",b,"-",x2,y2
    
    r=1

    while r > 0:
        r = a%b
        q = a//b
        x = x1-(x2*q)
        y = y1-(y2*q)
        
        if r != 0:
            print r,q,x,y
            a = b
            b = r
            x1 = x2
            x2 = x
            y1 = y2
            y2 = y
        else:
            print r,q,"-","-"

    print "---"