import pickle
def fn(datastore):
    for i in datastore:
        print(i,end='    ')
        for j in datastore[i]:
            if j != "parking":
                print(j,end="\t ")
                print(datastore[i][j][0])
                for k in range(1,len(datastore[i][j])):
                    print("\t\t\t",datastore[i][j][k])
            else:
                print("\n\t ",j,end="\t ")
                print(datastore[i][j])
                pass
        print("\n")
               
                       
               
               
def get_roomno():               #to get the room no
    try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return  
        o=int(input("Enter old new room"))
        n=int(input("Enter new value of room"))
    except:
        print("Room number should be integer")
        return
   
    set_roomno(b,d,o,n)
def set_roomno(b,d,o,n):        #to set the updated room number
    c=0
    for k in datastore[b][d]:
            for l in datastore[b][d][c]:
                    if l=="roomno" and datastore[b][d][c][l]==o:
                            datastore[b][d][c][l]=n
                            return
            c+=1
    print("No such room exist")
    return
def get_use():
   try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return  
        r=int(input("Enter room no"))
        n=input("Enter new usage")
   except:
        print("Room number should be integer")
        return
   set_use(b,d,r,n)
def set_use(b,d,r,n):               #to update the usage of room
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
    print("No such room exist")
    return                        
       
def get_size():                 #to get the size of the room
    try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return  
        r=int(input("Enter room no"))
        n=int(input("Enter new size"))
    except:
        print("Room number and size should be integer")
        return
   
    set_size(b,d,r,n)
def set_size(b,d,r,n):              #to update the size of the room
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
    print("No such room exist")
    return                  
def get_price():                #to get the price of the room
    try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return  
        r=int(input("Enter room no"))
        n=int(input("Enter new price"))
    except:
        print("Room number and price should be integer")
        return
   
    set_price(b,d,r,n)
def set_price(b,d,r,n):             #to set the price of the room
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
    print("No such room exist")
    return
def get_location():             #to get the location of parking
    b=input("Enter building")
    try:
        a=datastore[b]
    except:
        print("No such building exist")
        return
    d=input("Enter department")
    try:
        a=datastore[b][d]
    except:
        print("No such department exist")
        return    
    n=input("Enter new location")
    set_location(b,d,n)
def set_location(b,d,n):            #to set the location of parking
    for k in datastore[b][d]:    
            if k=="location" :
                    datastore[b][d][k]=n
                    return
def get_style():                    #to get the style of parking
    b=input("Enter building")
    try:
        a=datastore[b]
    except:
        print("No such building exist")
        return
    d=input("Enter department")
    try:
        a=datastore[b][d]
    except:
        print("No such department exist")
        return    
    n=input("Enter new style")
    set_style(b,d,n)
def set_style(b,d,n):               #to set the style of parking
    for k in datastore[b][d]:    
            if k=="style" :
                    datastore[b][d][k]=n
                    return
def getp_price():                   #to get the new parking price
    b=input("Enter building")
    try:
        a=datastore[b]
    except:
        print("No such building exist")
        return
    d=input("Enter department")
    try:
        a=datastore[b][d]
    except:
        print("No such department exist")
        return    
    n=int(input("Enter new price"))
    setp_price(b,d,n)
def setp_price(b,d,n):                  #to set the parking price
    for k in datastore[b][d]:    
            if k=="price" :
                    datastore[b][d][k]=n
                    return                        

def get_newb():                     #to get new building
    n=input("Enter unique name of new building")
    try:
        if n in datastore:
            a=datastore[n]
            a=1/0
        datastore[n]={}
    except:
        print("Building already exists")
   

def get_newd():                     #to get new department
    try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
        d=input("Enter name of department")
        t=input("Enter type of department : parking/medical")
        set_newd(b,d,t)
    except:
        print("Building and department should be string and room number must be positive numeric present in datastore")
   
def set_newd(b,d,t):
    if t=="medical":
        datastore[b][d]=[]
    else:
        datastore[b][d]={}
       
def get_roominfo():             #to get the info of new rooms
    try:
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
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
    except:
        print("Building and department should be string and room number must be positive numeric present in datastore")

def set_roominfo(b,d,n):                    #to set the new room info
    datastore[b][d].append({"roomno":n,"use":input("Enter usage"),"sq-ft":int(input("Enter size of room")),"price":int(input("Enter price of room"))})

def get_newp():         #to get the details of new parking
    try:  
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return    
        if d=="parking":
                set_newp(b,d)
        else:
                print("You can't add parking info, this department consists of rooms.Kindly select parking department")
                return
    except:
        print("Building and department should be string and room number must be positive numeric present in datastore")
           
def set_newp(b,d):                                      #to add new parking info
    datastore[b][d]["location"]=input("Enter location")
    datastore[b][d]["style"]=input("Enter style")
    datastore[b][d]["price"]=int(input("Enter price"))

def get_db():                               #to delete a building
    try:  
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        del datastore[b]                    #building deleted
   
    except:
            print("Building and department should be string and room number must be positive numeric present in datastore")
   
       
def get_dd():                               #to delete a department
    try:  
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return
        del datastore[b][d]                 #dept deleted
    except:
            print("Building and department should be string and room number must be positive numeric present in datastore")

def get_dr():                   #get the details of the room to be deleted
    try:      
        b=input("Enter building")
        try:
            a=datastore[b]
        except:
            print("No such building exist")
            return
        d=input("Enter department")
        try:
            a=datastore[b][d]
        except:
            print("No such department exist")
            return
        if d!="parking":
            n=int(input(("Enter unique roomno")))
        else:
            print("You can't delete rooms from parking")
            return
        set_dr(b,d,n)
    except:
            print("Building and department should be string and room number must be positive numeric present in datastore")
def set_dr(b,d,n):                  #delete room and its info
    c=0
    for k in datastore[b][d]:
            for l in datastore[b][d][c]:
                    if l=="roomno" and datastore[b][d][c][l]==n:
                            del datastore[b][d][c]
                            return
       
f_i=open('datastore_file.py','rb')
datastore=pickle.load(f_i)
f_i.close()
print(datastore)
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
    elif n==4:
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
    print(datastore)
    print("----------------------------------------------------Commited-----------------------------------------------------")
f_i=open('datastore_file.py','rb')
pickle.dump(datastore,f_i)
f_i.close()
