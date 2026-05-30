def Prime_factor_generator(n:int):
    i=2
    factors=[[],[]]
    while(i<n**0.5 +1):
        if(n%i==0):
            factors[0].append(i)
            count=0
            while(n%i==0):
                n//=i
                count+=1
            factors[1].append(count)
        i+=1
    if(n>1):
        factors[0].append(n)
        factors[1].append(1)
    return factors

print(Prime_factor_generator(600851475143))
