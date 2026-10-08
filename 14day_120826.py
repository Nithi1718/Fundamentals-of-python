# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make=make
#         self.model=model
#         self.year=year
#
#
# class Car(Vehicle):
#     def gear(self, no):
#         print(f"The Car is Moving in {no}th Gear")
#
# car=Car("BMW","Nexus",2026)
# car.gear(3)


# class Truck:
#     def __init__(self, speed, direction, color):
#         self.speed = speed
#         self.direction = direction
#         self.color = color
#     def get_info(self):
#         print(f"The truck is moving in {self.direction} direction in {self.speed}Km speed")
#
# class Train:
#     def __init__(self, start, destination):
#         self.start = start
#         self.destination = destination
#
#     def info(self):
#         print("Hi there")
#
# class Vehicle(Truck, Train):
#     def det(self, speed, direction, color):
#         print(speed, direction, color)
#
# c=Vehicle(25, 'North',"Black")
# c.get_info()
# c.info()



# class Grandpa:
#     def __init__(self, property):  ## There is no need to initialise it... if we need it we can use
#         self.property = property
#
#     def land(self):
#         print("Grandpa has the property of length of 25 Acres")
#
#
# class Father(Grandpa):
#
#     def house(self,count):
#         print(f"My Father has {count} houses")
#
# class Child(Father):
#     def bike(self):
#         print("I have 5 bikes")
#
# c=Child(0)
# c.house(3)
# c.land()
# c.bike()


# class Parent:
#     def __init__(self, office, business):
#         self.office = office
#         self.business = business
#     def salary(self,office, business):
#         print(f"The salary was credited")
#         print(office, business)
#
# class Son(Parent):
#     print(f"I am his first child i need 30000")
#     def rent(self, pg):
#         print(f"I need to pay rent for {pg} pg")
#
# class Girl(Parent):
#     def makeup(self):
#         print(f"Dad, I need for make up myself")
#
# girl=Girl(25000,30000)
# girl.makeup()
# boy=Son(25000,30000)
# boy.rent(4)
#
# girl.salary(2,3)


# class Father:
#     def house(self, rent):
#         print(f"The house is rented for the {rent} for one month")
#
# class Son:
#     def bike(self):
#         print("Hi Dad i have my bike")

# class School:
#     def source(self):
#         print("Source of the school is land surface")
#
# class Staff(School):
#     def source1(self):
#         print("Source of the staff is School")
#
# class Student(Staff, School):
#     def source2(self):
#         print("Student is the backbone of the school and country")
#
# a=Student()
# a.source1()
# a.source2()

