def countPairs(a,b,s):
    c=0
    for i in a:
        if s-i in b:
            c+=b.count(s-i)
    return c

a=list(map(int,input("Enter elements").split()))
b=list(map(int,input("Enter elements").split()))
s=int(input("Enter sum"))

print(countPairs(a,b,s))
