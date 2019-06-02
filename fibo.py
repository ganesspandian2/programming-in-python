#PROGRAM TO FIND THE FIBONACCI SERIES UPTO n
import functools
@functools.lru_cache(maxsize=None)

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)

n=int(input())       
for i in range(n):
    print(fibo(i))

