def Square_Sum(n:int):
    return(n*(n+1)*(2*n+1)//6)
#print(Square_Sum(10))

def Linear_Sum(n:int):
    return(n*(n+1)//2)
#print(Linear_Sum(10)**2)

def Problem(n:int):
    return Linear_Sum(n)**2 - Square_Sum(n)
print(Problem(100))