def original_triangles(lim:int):
    return lim**2

def axial_triangles(lim:int):
    return 2* lim**2

def line_generators(lim:int):
    lines={1.0:[1,1]}
    for i in range(1,lim+1):
        for j in range(1,i):
            if(j/i in lines):
                continue
            else:
                lines[j/i]=[i,j]
    return lines
l=(line_generators(20))
#print(l)


def special_triangles(lim:int):
    l= line_generators(lim)
    #let the line coordinates be (i,j) 
    # the set of similar streched lines are (ai,aj)
    # the perpendicular line to this is either (j,-i) or (-j,i)
    # the sum combination of these gives either (ai+bj , aj-bi) or (ai-bj , aj+bi)
    # 
    s=0
    for n in l:
        i,j = l[n][0],l[n][1]
        a,b=1,1
        while(False):
            pass
    return s
print(special_triangles(2))



def total_right_triangles(lim:int):
    return original_triangles(lim)+axial_triangles(lim)+special_triangles(lim)

#print(total_right_triangles(2))