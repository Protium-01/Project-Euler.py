def Factors(n:int):
    i=2
    f=[[],[]]
    while(i<=n**0.5+1):
        if(n%i==0):
            f[0].append(i)
            count=0
            while(n%i==0):
                n//=i
                count+=1
            f[1].append(count)
        i+=1
    
    if(n>1):
        f[0].append(n)
        f[1].append(1)
    return f
#print(Factors(4))

def factor_sum(n:int):
    f= Factors(n)
    s=1
    for i in range(len(f[0])):
        s*=(f[0][i]**(f[1][i] +1) - 1)//(f[0][i]-1)
    return s-n
#print(factor_sum(4))

def amicable_chain(lim:int):
    ac={1 : 1}
    for i in range(2,lim+1):
        ac[i]=factor_sum(i)
    
    return ac
print(amicable_chain(100))