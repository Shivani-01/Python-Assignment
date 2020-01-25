n=int(input("Enter number of players"))
d={}
for _ in range(1,n+1):
    d[_]={'type':input('Enter type of player'),'name':input('Enter name of player'),'matches':int(input("Enter total number of matches")),'runs':int(input("Enter total number of runs")),'average':int(input("Enter average")),'hihest_score':int(input("Enter highest score"))}
    print()
print(d)
