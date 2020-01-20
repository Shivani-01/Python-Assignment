n=int(input("Enter a pocket number"))
if n>36:
    print("Error!! Pocket number out of range")
else:
    if(n==0):
        print("Pocket is green")
    elif(n>=1 and n<=10):
        if(n%2==0):
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif n>=11 and n<=18:
        if n%2==0:
            print("Pocket is red")
        else:
            print("Pocket is black")
    elif n>=19 and n<=28:
        if n%2==0:
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif n>=29 and n<=36:
        if n%2==0:
            print("Pocket is red")
        else:
            print("Pocket is black")

