#atividade de lab 2.2

n = input()

for x in range(n):
    a,b = input()
    print a
    print b
    r=1

    while(r>0):
        r = a%b
        print r
        a = b
        b = r

    print "---"       

        
        