a=input().split(',')
b=list(map(int,a[1:]))
print(str(a[0])+" obtained "+str(sum(b[0:5]))+" marks out of 500 in theory and "+str(sum(b[5:]))+" marks out of 150 in practical and successfully passed the exam with "+str("{0:.2f}".format((sum(b)*100/650)))+" percentage ,Many Many Congratulations!")   

