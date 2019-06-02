#PROGRAM TO CHECK WHELTER THE NUMBER IS A STRONG NUMBER or NOT
import math
n=int(input("ENTER THE NUMBER\n"))
s=str(n)    

total=0
for i in s:
    total+=math.factorial(int(i))    

if total==n:
    print("The given number is a Strong Number")
else:
    print("The given number is not a Strong Number")    

