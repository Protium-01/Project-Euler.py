def is_pentagonal(n:int):
    a=(1+(1+24*n)**0.5)/6
    if(a==int(a)):
        return True
    else:
        return False
def pentagonal(n:int):
    return n*(3*n-1)//2

def check_pentagonal():
    p=[pentagonal(1)]
    i=2
    while(True):
        t=pentagonal(i)
        print(i)
        for a in p:
            if(is_pentagonal(a+t) and is_pentagonal(t-a)):
                return t-a
        p.append(t)
        i+=1
    
print(check_pentagonal())