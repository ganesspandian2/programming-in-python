#PROGRAM TO FIND THE SUM OF DIGITS IN A GIVEN NUMBER
n=input("ENTER THE NUMBER\n")
sum=0    
for i in range(len(n)):
    sum+=int(n[i])
print(sum)    


    