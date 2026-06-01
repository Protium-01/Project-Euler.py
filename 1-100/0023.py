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

def abundant_numbers(lim:int):
    a_n=[]
    for i in range(4,lim):
        s=factor_sum(i)
        if(s>i):
            a_n.append(i)
    return a_n
#print(len(abundant_numbers(28124)))

def abundant_sums(lim:int):
    a_n_l=abundant_numbers(28124)
    a_s={1 : True}
    for i in range(1,lim):
        a_s[i]=True
    sum=0
    for i in a_n_l:
        for j in a_n_l:
            a_s[i+j]=False
    for i in range(1,lim):
        if(a_s[i]):
            sum+=i
    return sum
print(abundant_sums(28124))