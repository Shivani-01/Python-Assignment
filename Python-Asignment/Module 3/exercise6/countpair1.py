l=list(map(int,input("Enter elements").split()))
s=int(input("Enter sum"))
a=list(set(l))
c=0
d={}
for i in range(len(a)):
    d[a[i]]=l.count(a[i])
for j in sorted(d.keys()):
    if s-j==j:
        c+=(d[j]*(d[j]-1)//2)
        continue
    if s-j in  d and (s-j)>j:
        c+=(d[j]*d[s-j])
print(c)
       
