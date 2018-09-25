a=int(input("Enter the number:"))
if a in range(0,100000000000):
    if(a%2==0):
        print("Even")
    elif(a%2!=0):
        print("Odd")
else :
    print("invalid")
