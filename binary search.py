a=[]
size=int(input("ENTER THE SIZE OF LIST\n"))
for i in range(size):
    x=int(input("ENTER THE NUMBER\n"))
    a.append(x)
a.sort()
n=int(input("ENTER THE NUMBER TO BE SEARCHED\n"))

l=0 
r=size-1
while 0<len(a):
    m=int((l+r)/2)
    if a[m]<n:
        l=m+1

    elif a[m]>n:
        r=m-1

    elif a[m]==n:
        print("ELEMENT FOUND IN",m+1)
        break
