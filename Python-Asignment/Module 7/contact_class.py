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

a=Contact(input("Enter name"),int(input("Enter phone")),input("Enter email"))
print(a.__str__())
print("update the values")
print("Old value of name",a.get_name() )
a.set_name()
print("Old value of phone number",a.get_phone() )
a.set_phone()
print("Old value of email",a.get_email() )
a.set_email()
print(a.__str__())