def factorial(n:int):
    if(n==0):
        return 1
    return n*factorial(n-1)
print(factorial(9))

def Lexicographic_String(arr:list[str],n:int):
    a=[]
    c=0
    t=factorial(len(arr)-1)
    for i in range(len(arr)-1,0,-1):
        a.append((n-c-1)//t)
        c+=a[-1]*t
        t//=i
    a.append(n-c-1)
    s=""
    while(len(a)!=0):
        s+=arr[a[0]]
        arr.pop(a[0])
        a.pop(0)
    return a,s
print(Lexicographic_String(['0','1','2','3','4','5','6','7','8','9'],10**6))