def even_fibonacci_array_generator(end:int):
    arr=[2,8]
    while(arr[-1]<end):
        arr.append(next_even_fibonacci(arr[-2],arr[-1]))
    arr=arr[:-1]
    return arr

def next_even_fibonacci(n_1:int,n_2:int):
    return 4*n_2 + n_1

print(sum(even_fibonacci_array_generator(4*10**6)))