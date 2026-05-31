def problem():
    str=[['one','two','three','four','five','six','seven','eight','nine'],['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'],['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'],['hundred','thousand']]
    count1,count2,count3,count4,count5=0,0,0,0,0
    for i in str[0]:
        count1+=len(i)
    for i in str[1]:
        count2+=len(i)
    for i in str[2]:
        count3+=len(i)*10
    count3+=count1*len(str[2])
    count4+=(count1+9*len(str[3][0]))*100
    count4+=(99*3+count3+count2+count1)*len(str[0])
    count5+=len(str[0][0])+len(str[3][1])
    r=[count1,count2,count3,count4,count5]
    return sum(r)
print(problem())