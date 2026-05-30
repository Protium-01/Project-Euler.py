#need optimization
# i think it could be solved by polygonal sums
def Lattice_Paths(m:int,n:int):
    #Assume a array of m*n size
    arr=[[1 for i in range(m+1)]]
    for i in range(1,n+1):
        arr.append([1])
        for j in range(1,m+1):
            arr[-1].append(arr[i-1][j]+arr[i][j-1])      
    return arr[-1][-1]
print(Lattice_Paths(20,20))