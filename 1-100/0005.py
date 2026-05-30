def lcm(arr:list[int]):
    i=2
    multiple=1
    tem=arr.copy()
    while(len(tem)):
        b=0
        a=0
        while(a<len(tem)):
            if(tem[a]%i==0):
                tem[a]//=i
                b=1
            if(tem[a]==1):
                tem.remove(1)
            a+=1
        if(b):
            multiple*=i
        else:
            i+=1
        print(tem,multiple)
    return multiple
print(lcm([i for i in range(1,20)]))