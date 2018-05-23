#atividade de lab 2.1

n = input() 

for x in range(n):
    a,b = input()
    q=0
    r=a
    print q,r

    while(r>=b):
        q+=1
        r-=b
        print q,r
    
    print "---"     




