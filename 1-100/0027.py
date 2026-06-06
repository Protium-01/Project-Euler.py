def Prime_Generator(lim:int):
    p=[2]
    for i in range(3,lim+1):
        for j in p:
            if(i<j**2):
                p.append(i)
                break
            if(i%j==0):
                break
    return p
#print(Prime_Generator(1000))

def Quadratic_primes(lim:int):
    pr=Prime_Generator(lim**2)    
    b=[]
    for i in pr:
        if(i>lim):
            break
        b.append(i)    
    Pairs=[]
    for j in b:
        for i in range(-j,j+1):
            if((1+i+j) in pr):
                if((4+2*i+j) in pr):
                    Pairs.append([i,j])
                    print(i,j)
    n=2
    while(len(Pairs)>1):
        print(n)
        for i in Pairs:
            if(n**2 + i[0]*n + i[1] not in pr):
                Pairs.remove(i)
        n+=1
    return Pairs
print(Quadratic_primes(1001))