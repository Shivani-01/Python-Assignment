from automobile import Auto

class Car(Auto):
    def __init__(self,__make,__model,__mileage,__price,__doors):
        Auto.__init__(self,__make,__model,__mileage,__price)
        self.__doors=__doors
    def get_doors(self):
        return self.__doors
    def set_doors(self,doors):
        self.__doors=doors
    

a=Car(2009,"suv",50,5555,2)
print(a.get_doors())
print(a.get_make())
a.set_make(52)
print(a.get_make())
print(a.get_model())
a.set_doors(4)
print(a.get_doors())

