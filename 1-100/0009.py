def Pythogoras_Triplets(sum:int):
    if(sum%2!=0):
        return []
    a=1
    arr=[]
    while(a<sum/(2+2**0.5)):
        b=sum*(sum-2*a)/(2*(sum-a))
        if(int(b)==b):
            arr.append([a,int(b),int(sum-(a+b))])
        a+=1
    return arr
a=Pythogoras_Triplets(1000)
print(a[0][0]*a[0][1]*a[0][2])
