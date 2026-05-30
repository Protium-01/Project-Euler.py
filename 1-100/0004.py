def is_palindrome(n:int):
    s=str(n)
    i=0
    while(i<len(s)/2 + 1):
        if(s[i]!=s[-i-1]):
            return False
        i+=1
    return True
#print(is_palindrome(101))

def max_n_digit_palindrome_product(n:int):
    #Constraints:
    #1. n_1*n_2 = palindrome
    #2. n_1*n_2 -> max
    pal=0
    for i in range(0,10**n -1):
        b=1
        for j in range(0,i//2 +1):
            pdt = (10**n - i+j)*(10**n - j)
            if(pal<pdt):
                if(is_palindrome(pdt)):
                    pal=pdt
                b=0
        if(b):
            return pal
print(max_n_digit_palindrome_product(3))