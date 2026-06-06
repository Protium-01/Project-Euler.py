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
print(sum(Prime_Generator(2*10**6)))