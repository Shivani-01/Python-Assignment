from automobile import Auto

class Truck(Auto):
    def __init__(self,__make,__model,__mileage,__price,__drivetype):
        Auto.__init__(self,__make,__model,__mileage,__price)
        self.__drivetype=__drivetype
    def get_drivetype(self):
        return self.__drivetype
    def set_drivetype(self,drivetype):
        self.__drivetype=drivetype
    

a=Truck(2009,"suv",50,5555,2)
print(a.get_drivetype())
print(a.get_make())
a.set_make(52)
print(a.get_make())
print(a.get_model())
a.set_drivetype(4)
print(a.get_drivetype())

