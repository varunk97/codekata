a=int(input("Enter the number:"))
if a in range(0,100000000000):
    if(a%2==0):
        print("even")
    elif(a%2!=0):
        print("odd")
else :
    print("invalid")
