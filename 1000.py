def AND_Array(n:int):
    a=[]
    for i in range(1,n+1):
        a.append([])
        for j in range(1,n+1):
            if(i==j):
                a[-1].append(0)
            else:
                a[-1].append(i&j)
    return a

def I(n:int):
    
    arr=AND_Array(n)
    CORELAP=arr.copy()
    s=[sum(i) for i in arr]
    A=[s.index(max(s))]
    B=[arr[A[0]].index(max(arr[A[0]]))]
    for i in range(n):
        arr[i][A[0]]=0
        arr[i][B[0]]=0
    while(len(arr)>len(A)+len(B)):
        a=[]
        b=[]
        print(len(A),len(B))
        for i in range(n):
            a.append(0)
            for j in B:
                a[i]+=arr[j][i]
            b.append(0)
            for j in A:
                b[i]+=arr[j][i]
        if(max(a)<=max(b)):
            B.append(b.index(max(b)))
            for i in range(n):
                arr[i][B[-1]]=0
        else:
            A.append(a.index(max(a)))
            for i in range(n):
                arr[i][A[-1]]=0
    s=0
    for i in A:
        for j in B:
            s+=(i+1)&(j+1)
    return A,B,s
print(I(1000))