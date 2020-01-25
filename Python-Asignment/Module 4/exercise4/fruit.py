d={}
d['apple']={'bname':'app','producers':['China','US','Turkey'],'nutrition':{'carbohydrates':13.81,'fat':0.17,'protein':0.26}}
d['banana']={'bname':'app','producers':['US','Turkey'],'nutrition':{'carbohydrates':13.81,'fat':0.17,'protein':1.26}}
d['mango']={'bname':'app','producers':['China','Turkey'],'nutrition':{'carbohydrates':13.81,'fat':0.17,'protein':0.56}}

#highest protein value
p=[]
for i in d:
    for j in d[i]:
        if j=='nutrition':
            for k in d[i][j]:
                if k =='protein':
                    p.append(d[i][j][k])
    
i=p.index(max(p))
c=0
for j in d:
    if c==i:
        print(j)
    c+=1
del p
#china
f=0
p=[]
a=[]
for i in d:
    for j in d[i]:
        if j=='producers':
            if 'China' in d[i][j]:
                f=1
        if j=='nutrition' and f==1:
            for k in d[i][j]:
                if k =='protein':
                    p.append(d[i][j][k])
                    f=0
                    a.append(i)
i=p.index(max(p))
print(a[i])
                    

    
