import pickle
class Contact:
    def __init__(self,__name,__phone,__email):
        self.__name=__name
        self.__phone=__phone
        self.__email=__email
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def set_name(self):
        self.__name=input("Enter name")
    def set_phone(self):
        self.__phone=int(input("Enter phone"))
    def set_email(self):
        self.__email=input("Enter email")
    def __str__(self):
        return f'name : {self.__name} phonenumber : {self.__phone} emailaddress : {self.__email}'




o=open('contact.txt','rb')
b=pickle.load(o)
o.close()
m=1
for i in b:
   if i>m:
       m=i
q_=m

while(1):
    print("\t\tEnter choice")
    n=int(input(" 1 to enter new record\n 2 to update a record\n 3 to view all records\n 4 to view a particular record\n 5 to delete a particular record\n 6 to delete all records\n0 to exit"))
    if n==1:
        a=Contact(input("Enter name"),int(input("Enter phone")),input("Enter email"))
        print("record num=",q_,a.__str__())
        b[q_]=a
        q_+=1
        
    elif n==2:
        i=int(input("Enter record num"))
        c=b[i]
        c.get_name()
        c.get_phone()
        c.get_email()
        c.set_email()
        c.set_phone()
        c.set_name()
        print(c.__str__())
    elif n==3:
        for d in b:
            print(b[d].__str__())
    elif n==4:
        p=int(input("Enter record number"))
        print(b[p])
    elif n==5:
        p=int(input("Enter record number"))
        del b[p]
    elif n==6:
        del b
        b={}
    elif n==0:
        break
    print()
    o=open('contact.txt ','wb')
    pickle.dump(b,o)
    o.close()

