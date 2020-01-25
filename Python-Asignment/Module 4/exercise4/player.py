squad={'Batsmen':{'Rohit Sharma':{'Matches':206,'Runs':8010,'Average':47.4,'Highest_score':264},'Rohit Sharma':{'Matches':206,'Runs':8010,'Average':47.4,'Highest_score':264},'Rohit Sharma':{'Matches':206,'Runs':8010,'Average':47.4,'Highest_score':264},'Shikhar Dhawan':{'Matches':128,'Runs':5355,'Average':44.62,'Highest_score':143},'Virat Kohli':{'Matches':227,'Runs':10843,'Average':59.58,'Highest_score':183}}}
r=[]
a=[]
m=[squad[i][j][k] for i in squad for j in i for k in j if k=='Highest_score']
print(m)
for i in squad:   
    for j in squad[i]:      
        for k in squad[i][j]:           
            if k=='Highest_score':
                r.append(squad[i][j][k])
                
        a.append(j)
i=r.index(max(r))
print(a[i],r[i])
