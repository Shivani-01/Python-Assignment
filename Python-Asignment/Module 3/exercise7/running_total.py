n,m=map(int,input().split())
l=list(map(int,input().split()))
h=0
for i in range(n):
    if(i+m<=n):
        if h < sum(l[i:i+m]):
            h=sum(l[i:i+m])
    else:
        if h < (sum(l[i:])+sum(l[0:m+i-n])):
            h=sum(l[i:])+sum(l[0:m+i-n])
print(h)
