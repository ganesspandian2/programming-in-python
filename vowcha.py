def isvowel(s):
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            return True
    return False

s=input()
if isvowel(s):
    print("The given character is Vowel")
else:
    print("The given character is Consonant")    

