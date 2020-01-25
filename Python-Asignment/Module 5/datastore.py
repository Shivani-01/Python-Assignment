def fn(datastore):
    for i in datastore:
        if i=="None":
            break
        print(i,end='    ')
        for j in datastore[i]:
            if j is not "parking":
                print(j,end="\t ")
                print(datastore[i][j][0])
                for k in range(1,len(datastore[i][j])):
                    print("\t\t\t",datastore[i][j][k])
            else:
                print("\n\t ",j,end="\t ")
                print(datastore[i][j])
        print("\n")
           
               
           
           
def get_roomno():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    o=int(input("Enter old new room"))
    n=int(input("Enter new value of room"))
    set_roomno(b,d,o,n)
def set_roomno(b,d,o,n):
    c=0
    for k in datastore[b][d]:
        for l in datastore[b][d][c]:
            if l=="roomno" and datastore[b][d][c][l]==o:
                datastore[b][d][c][l]=n
                return
        c+=1
def get_use():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    r=int(input("Enter room no"))
   
    n=input("Enter new usage")
    set_use(b,d,r,n)
def set_use(b,d,r,n):
    c=0
    f=0
    for k in datastore[b][d]:
        for l in datastore[b][d][c]:
            if l=="roomno"and datastore[b][d][c][l]==r:
                f=1
            if l=="use" and f==1 :
                datastore[b][d][c][l]=n
                return
        c+=1                        
       
def get_size():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    r=int(input("Enter room no"))
    n=int(input("Enter new size"))
    set_size(b,d,r,n)
def set_size(b,d,r,n):
    c=0
    f=0
    for k in datastore[b][d]:
        for l in datastore[b][d][c]:
            if l=="roomno"and datastore[b][d][c][l]==r:
                f=1
            if l=="sq-ft" and f==1 :
                datastore[b][d][c][l]=n
                return
        c+=1                        
def get_price():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    r=int(input("Enter room no"))
    n=int(input("Enter new price"))
    set_price(b,d,r,n)
def set_price(b,d,r,n):
    c=0
    f=0
    for k in datastore[b][d]:
        for l in datastore[b][d][c]:
            if l=="roomno"and datastore[b][d][c][l]==r:
                f=1
            if l=="price" and f==1 :
                datastore[b][d][c][l]=n
                return
        c+=1  
def get_location():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    n=input("Enter new location")
    set_location(b,d,n)
def set_location(b,d,n):
    for k in datastore[b][d]:    
        if k=="location" :
            datastore[b][d][k]=n
            return
def get_style():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    n=input("Enter new style")
    set_style(b,d,n)
def set_style(b,d,n):
    for k in datastore[b][d]:    
        if k=="style" :
            datastore[b][d][k]=n
            return
def getp_price():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    n=int(input("Enter new price"))
    setp_price(b,d,n)
def setp_price(b,d,n):
    for k in datastore[b][d]:    
        if k=="price" :
            datastore[b][d][k]=n
            return                        

def get_newb():
    n=input("Enter unique name of new building")
    datastore[n]={}
   
def get_newd():
    b=input("Enter the building")
    d=input("Enter name of department")
    t=input("Enter type of department : parking/medical")
    set_newd(b,d,t)
def set_newd(b,d,t):
    if t=="medical":
        datastore[b][d]=[]
    else:
        datastore[b][d]={}
       
def get_roominfo():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    if d!="parking":
        n=int(input(("Enter unique roomno")))
        c=0
        r=[]
        for i in datastore[b][d]:
            for j in datastore[b][d][c]:
                r.append(datastore[b][d][c]["roomno"])
            c+=1
        if n in r:
            print("This room number is already assigned")
            get_roominfo()
        set_roominfo(b,d,n)
    else:
        print("You can't add rooms to parking")
        return

def set_roominfo(b,d,n):
    datastore[b][d].append({"roomno":n,"use":input("Enter usage"),"sq-ft":int(input("Enter size of room")),"price":int(input("Enter price of room"))})
   
def get_newp():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    if d=="parking":
        set_newp(b,d)
    else:
        print("You can't add parking info, this department consists of rooms.Kindly select parking department")
        return
       
def set_newp(b,d):
    datastore[b][d]["location"]=input("Enter location")
    datastore[b][d]["style"]=input("Enter style")
    datastore[b][d]["price"]=int(input("Enter price"))
   
def get_db():
    b=input("Enter building you want to delete")
    if b not in datastore:
        print("No such building exist")
        return
    del datastore[b]
       
def get_dd():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    del datastore[b][d]

def get_dr():
    b=input("Enter building")
    if b not in datastore:
        print("No such building exist")
        return
    d=input("Enter department")
    if d not in datastore[b]:
        print("No such department exist")
        return
    if d!="parking":
        n=int(input(("Enter unique roomno")))
    else:
        print("You can't delete rooms from parking")
        return
    set_dr(b,d,n)
def set_dr(b,d,n):
    c=0
    for k in datastore[b][d]:
        for l in datastore[b][d][c]:
            if l=="roomno" and datastore[b][d][c][l]==n:
                del datastore[b][d][c]
                return
   
datastore={"office":{"medical":[{"roomno":100,"use":"waiting","sq-ft":50,"price":75},{"roomno":101,"use":"waiting","sq-ft":250,"price":75},{"roomno":102,"use":"examination","sq-ft":125,"price":150},{"roomno":103,"use":"examination","sq-ft":125,"price":150},{"roomno":104,"use":"office","sq-ft":150,"price":100}],"parking":{"location":"premium","style":"covered","price":750}}}
while(1):
    print("\tEnter choice")
    print("1  --- print current structure\n2  --- add new fields\n3  --- update existing fields\n4  --- delete existing fields\n0  --- exit")
    n=int(input())
    if n==1:
        print(fn(datastore))    
        continue
    if n==2:
        print("\tEnter choice")    
        print("1  --- adding new building\n2  --- adding new department\n3 --- adding new room\n4  --- adding parking information\n0  --- back")
        i=int(input())
        if i==1:
            get_newb()
        elif i==2:
            get_newd()
        elif i==3:
            get_roominfo()
        elif i==4:
            get_newp()
        elif i==0:
            continue
    elif n==3:
        print("\tEnter choice")
        print("1  --- updating room number\n2  --- updating new usage of room\n3  --- updating room size\n4  --- updating room price\n5  --- updating location\n6  --- updating style\n7  --- updating parking price\n0  --- back")
        i=int(input())
        if i==1:
            get_roomno()
        elif i==2:
            get_use()
        elif i==3:
            get_size()
        elif i==4:
            get_price()
        elif i==5:
            get_location()
        elif i==6:
            get_style()
        elif i==7:
            getp_price()
        elif i==0:
            continue
    elif n==3:
        print("\tEnter choice")
        print("1  --- delete a building\n2  --- delete a department\n3  --- delete roomnumber and its info\n4  --- delete whole data\n0  --- back")
        i=int(input())
        if i==1:
            get_db()
        elif i==2:
            get_dd()
        elif i==3:
            get_dr()
        elif i==0:
            continue
   
    elif n==0:
        break
    print(fn(datastore))
    print("----------------------------------------------------Commited-----------------------------------------------------")
