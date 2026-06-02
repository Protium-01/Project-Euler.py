def count_cycles(n:int):
    i=1
    r=[1]
    while(True):
        i=(i*10)%n
        if(i in r):
            break
        r.append(i)
    return len(r)
#print(count_cycles(7))

def max_cycle_len(lim:int):
    m=1
    v=0
    for i in range(1,lim):
        c=count_cycles(i)
        if(c>m):
            m=c
            v=i
    return v,m
print(max_cycle_len(1000))