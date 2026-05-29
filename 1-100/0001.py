#Solved
#O_t(1)
#O_s(1)

def Sum_Multiples_of_m_or_n(m :int, n :int, start :int, end :int):
    end = end - 1
    return Sum_Multiples_of_n(m,start,end)+Sum_Multiples_of_n(n,start,end)-Sum_Multiples_of_n(m*n,start,end)

def Sum_Multiples_of_n(n :int, start :int, end :int):
    return n*(n_sum(end//n) - n_sum(start//n))

def n_sum(n :int):
    return n*(n+1)//2

print(Sum_Multiples_of_m_or_n(3,5,0,1000))