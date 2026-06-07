def Triangular_Number(n:int):
    return n*(n+1)//2

def factors(n:int):
    f=[[],[]]
    i=2
    while(i<n**0.5+1):
        if(n%i==0):
            f[0].append(i)
            c=0
            while(n%i==0):
                n//=i
                c+=1
            f[1].append(c)
        i+=1
    if(n!=1):
        f[0].append(n)
        f[1].append(1)
    return f
#print(factors(15))

def Factors_count(n:int):
    f=factors(n)
    c=1
    for i in f[1]:
        c*=(i+1)
    return c
#print(Factors_count(12))

def Highly_Divisible_Triangular_Number(n:int):
    i,num,f=1,1,1
    while(f<=n):
        i+=1
        num=Triangular_Number(i)
        f=Factors_count(num)
    return i,num,f
print(Highly_Divisible_Triangular_Number(500))