f=1
while(f):
    a=input("Enter positive whole sale price")
    if('-' in a):
        continue
    retail=int(a)*0.5/100
    print("Retail = ",retail)
    print("Do you want to enter more values? Enter 0 for no and 1 for yes")
    f=int(input())

    
    
