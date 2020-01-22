l=list(map(int,input("Enter elements").split()))
m=max(l)
a,b=[0]*(m+1),''
s=len(list(set(l)))
for i in set(l):
    a[i]=l.count(i)
for i in range(s):
    q=a.index(max(a))
    p=max(a)
    b+=''.join(str(q)*p)  
    a[q]=-1
print(list(map(int,b)))
