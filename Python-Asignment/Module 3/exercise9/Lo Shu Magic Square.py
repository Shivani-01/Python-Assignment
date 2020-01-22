n=int(input())
l=[]
k=0
while k!=n:
    l.append(list(map(int,input().split())))
    k+=1
r=[]
c=[]
d,d1=0,0
f=1
for i in range(n):
    r.append(0)
    for j in range(n):
        r[i]+=l[i][j]
for i in range(n):
    c.append(0)
    for j in range(n):
        c[i]+=l[j][i]
for i in range(n):
    for j in range(n):
        if i==j:
            d+=l[i][j]
        if i+j==n-1:
            d1+=l[i][j]

for i in range(n):
    if r[i]==c[i]==d==d1:
        continue
    else:
        print("False")
        f=0
        break
if(f):
    print("True")
