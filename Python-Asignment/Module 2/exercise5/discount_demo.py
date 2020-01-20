n=int(input("Enter number of packages purchased"))
d=0
if(n>=10 and n<=19):
    d=0.1*99
elif(n>=20 and n<=49):
    d=0.2*99
elif(n>=50 and n<=99):
    d=0.3*99
elif(n>=100):
    d=0.4*99
amt=99
da=amt-d
da*=n
if(d>0):
    print("Amount of discount:  $",d*n)
    print("Total amount of purchase after discount:  $",da)
else:
    print("Total amount of purchase:  $",da)
