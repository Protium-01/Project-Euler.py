def original_triangles(lim:int):
    return lim**2

def axial_triangles(lim:int):
    return 2* lim**2

def special_triangles(lim:int):
    l= line_generators(lim)
    #let the line coordinates be i ,j 
    # the set of similar streched lines are ai+bj
    # the perpendicular line to this is either aj-bi or bi-aj
    # the sum combination of these gives either (a-b)i + (a+b)j  or (a+b)i + (a-b)j
    # thus 2 criterion (a+b)i = lim and the second (a+b)j = lim
def line_generators(lim:int):
    lines={1.0:[1,1]}
    for i in range(1,lim+1):
        for j in range(1,i):
            if(j/i in lines):
                continue
            else:
                lines[j/i]=[[i,j]]
    return lines
l=(line_generators(20))
#print(len(l))

def total_right_triangles(lim:int):
    return original_triangles(lim)+axial_triangles(lim)+special_triangles(lim)
