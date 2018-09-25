d=['a','e','i','o','u','A','E','I','O','U']
s=input()
if s.isalpha():
    if(s in d):
        print("Vowel")
    else :
        print("Consonant")
else :
    print("invalid")
