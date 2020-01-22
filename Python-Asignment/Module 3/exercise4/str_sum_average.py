a=input().split(' ')
b=[int(a[i]) for i in range(2,len(a),3)]
print("Sum",sum(b),"Percentage is",round(sum(b)/len(b),2))
