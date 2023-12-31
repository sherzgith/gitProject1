# In this file we want to have execution only( objects)
from src.o_o_programming.car_class import *

# Create the object (instance of Vehicle class)
car1 = Car('mazda', '6', 2016)
car1.get_description()
# print(car1.model)  # you can do before hiding , after hiding you have to use get_description() method
print('---------------------------')
print(car1.get_odometer())
car1.set_odometer(10000)
print(car1.get_odometer())
# car1.odometer_reading = 5000 # does the same fob as car1.set_odometer(), when function does not have a logic

# How to restrict object updating attributes directly, so we can only set odometer using the function
# OOP concept - encapsulation, hide the attributes from the object ( or child classes)

print(car1.get_odometer())
car1.set_odometer(1000)  # testing the logic here
print(car1.get_odometer())
car1.set_odometer(20000)  # testing the logic here
print(car1.get_odometer())
car1.increment_odometer(50)
print(car1.get_odometer())
# car1.increment_odometer('a')
car1.increment_odometer(-50)
print(car1.get_odometer())

print('**************Creating the electric car object........')
lucid1 = ElectricCar('lucid', 'Y', 2023)
lucid1.get_description()
print(lucid1.get_odometer())
print('Battery size :', lucid1.battery_size)
# print(car1.battery_size) # parent does not have this attribute
# print(car1.describe_battery) # parent does not have this attribute
lucid1.describe_battery()


print('***************TESLA*********************')
tesla1 = ElectricCar('tesla', 'X', 2022, 88)
tesla1.get_description()
tesla1.describe_battery()
print("***************Method Overriding***************")
car1.get_description()
tesla1.get_description()






