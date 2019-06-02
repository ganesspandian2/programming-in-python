#PROGRAM TO FIND THE FACTORIAL OF A NUMBER
import functools
@functools.lru_cache(maxsize=None)

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
n=int(input())        
print(fact(n))