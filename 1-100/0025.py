def Fibonacci_sequence(lim:int):
    a=[1,1]
    while(a[-1]<lim):
        a.append(a[-1]+a[-2])
    return a[-1],len(a)
print(Fibonacci_sequence(10**999))