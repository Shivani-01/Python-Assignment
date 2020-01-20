n=int(input("Enter 5 digit number"))
a=0
while(n!=0):
    r=n%10
    a=a*10+r
    n//=10
print(a)
