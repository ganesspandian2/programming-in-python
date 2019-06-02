#PROGRAM TO CHECK WHELTER THE NUMBER IS A PERFECT NUMBER or NOT
n=int(input("ENTER THE NUMBER\n"))
total=0
for i in range(1,n,1):
    if n%i==0:
        total+=i

if total==n:
    print("The given number is a Perfect Number")
else:
    print("The given number is not a Perfect Number")