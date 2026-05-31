def Sundays(month:int,shift:int):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    sundays=days[month-1]-7+shift
    if(shift==0):
        sundays+=7
    return sundays//7 + 1
#print(Sundays(1,0))

def First_day_Sunday_counting(start:int,end:int,startshift:int):
    days_shift=[3,0,3,2,3,2,3,3,2,3,2,3]
    sum=0
    sum+=startshift
    first_sundays=0
    for i in range(start,end+1):
        for j in range(12):
            if(sum==0):
                first_sundays+=1
            if(j==1):
                if((i%100!=0 or i%400==0)and(i%4==0)):
                    sum+=1
            sum=(sum+days_shift[j])%7
    if(sum==0):
        first_sundays+=1
    return first_sundays

print(First_day_Sunday_counting(1901,2000,(1+366)%7))    

