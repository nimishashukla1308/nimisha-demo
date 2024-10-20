# class Person:
#     name="anonymous"
#     def change_name(self,name):
#         self.name=name

# p1=Person("Rahul Kumar")
# class student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.maths)/3+"%")+"%"
# stu1=student(99,98,90)
# print(stu1.percentage)
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        Car.total_car+=1
    def get_brand(self):
        return self.brand+"/"
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "petrol or diesel"
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size= battery_size
    def fuel_type(self):
        return "charge"


my_car=Car("toyota", "corolla")
print(my_car.brand) 
print(my_car.model)
print(my_car.full_name())
my_new_car=Car("Tata","Safari")
print(my_new_car.get_brand) 
print(my_new_car.model) 
my_tesla=ElectricCar("tesla","modern s","85kwh")
print(my_tesla.battery_size)
print(my_tesla.fuel_type)
