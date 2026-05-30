#need to optimise
def n_th_prime_generator(n:int):
    prime=[2]
    i=3
    while(len(prime)<n):
        b=1
        for j in prime:
            if(i%j==0):
                b=0
                break
            if(i<j**0.5 +1):
                break
        if(b):
            prime.append(i)
        i+=1
    return prime[-1]
print(n_th_prime_generator(10001))