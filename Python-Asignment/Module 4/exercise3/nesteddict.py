people={1:{'name':'John','age':'27','sex':'Male'},2:{'name':'Marie','age':'22','sex':'Female'}}
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='No'
print(people[3])
people[4]={'name':'Peter','age':'29','sex':'Male','married':'Yes'}
print(people[4])
del people[3]['married'], people[4]['married']
print(people[3])
print(people[4])
del people[3],people[4]
print(people)
for p_id,p_info in people.items():
    print('\nPerson id :',p_id)
    print(p_id,p_info)
    for key in p_info:
        print(key+':',p_info[key])
print(people.items())

