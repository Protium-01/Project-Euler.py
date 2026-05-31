#Took Long enough computation time
def Pythogoras_Triplet(sum:int):
    #x^2 + y^2 = z^2
    #x+y+z=sum
    arr=[]#triplets
    x=1
    lim=sum/(2+2**0.5)
    while(x<lim):
        if((sum**2 - 2*sum*x)%(2*sum - 2*x)==0):
            arr.append([x,int((sum**2 - 2*sum*x)/(2*sum - 2*x))])
        x+=1
    return arr
#print(Pythogoras_Triplet(120))

def Singular_Triplets(end:int):
    count=0
    for i in range(12,end+1,2):
        t=Pythogoras_Triplet(i)
        if(len(t)==1):
            print(t,i)
            count+=1
    return count
print(Singular_Triplets(15 * 10**5))