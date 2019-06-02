#PROGRAM TO FIND THE L.C.M OF GIVEN NUMBER
a=int(input("ENTER THE NUMBER\n"))
b=int(input("ENTER THE NUMBER\n"))    
while b!=0:    
    a,b=b,a%b
print("LCM is",a)    
