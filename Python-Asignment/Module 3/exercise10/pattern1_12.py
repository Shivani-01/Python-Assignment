#Plus star pattern
n=int(input("Enter a number for plus star pattern"))
for i in range(n):
    if(n%2!=0):
        if(i==n//2):
            print('*'*n)
        else:
            print(str(' '*(n//2))+'*'+str('  '*(n//2)))
    else:
        if(i==n//2 or i==n//2-1):
            print(' '+'*'*(n-1))
        else:
            print(str(' '*(n//2))+'*'+str('  '*(n//2)))

#Left arrow pattern
n=int(input("Enter odd integer for left arrow pattern"))
for i in range(n+1):
    if i<n//2:
        print('*'*(n//2-i),end='')
    elif i==n//2:
        continue
    else:
        print('*'*(n//2-n+i+1),end='')
    print()

#Hollow pyramid
n=int(input("Enter a number for hollow pyramid"))
print(str(' '*(n))+'*')
n-=1
for i in range(1,2*n-1,2):
    if i<n:
        print(str(' '*(n-i))+str('*')+str(' '*(2*i+1))+str('*'))

print('* '*(n+2))   

#Diamond star pattern
n=int(input("Enter odd number for diamond star pattern"))
for i in range(0,n):
    if i<n//2:
        print(str('  '*(n//2-i))+str('* '*(2*i+1))+str('  '*(n//2-i)))
    elif i==n//2:
        print('* '*n)
    else:
        print(str('  '*(i-n//2))+str('* '*(2*n-2*i-1))+str('  '*(i-n//2)))

