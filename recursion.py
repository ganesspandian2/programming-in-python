def recursion(a):
    a=(a**2)
    print(a)

a=int(input("ENTER THE NUMBER\n"))    
for i in range(a):
    recursion(i)

