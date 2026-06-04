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
#print(Factors(4**2))
def Factor_Count(n:int,power=1):
    counter=1
    f=Factors(n)
    for i in f[1]:
        if(power):
            counter*=(power*i+1)
        else:
            counter*=(i+1)
    return counter
#print(Factor_Count(12))

def Diophantine_Reciprocals_Count(n:int):
    return (Factor_Count(n,2)+1)//2
#print(Diophantine_Reciprocals_Count(4))

def Problem(len:int):
    m,v=1,1
    c=2
    while(m<=len):
        t=Diophantine_Reciprocals_Count(c)
        if(m<t):
            m=t
            v=c
        c+=1
    return v,m
print(Problem(1000))