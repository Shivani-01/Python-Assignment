n=int(input("Enter 5 digit number"))
i=0
a=0
while(i<5):
   r=n%10
   r+=1
   a+=((r%10)*(10**i))
   n//=10
   i+=1
print(a)
