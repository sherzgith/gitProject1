# Creating car model


class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_names(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
your_new_car = Car('mazda', '6', 2016)
print(my_new_car.get_descriptive_names())
print(your_new_car.get_descriptive_names())


print('********************************************END OF CAR*************************************************************')



class Vehicle:
    """Blue print to represent the general Vehicle"""
    # Constractor

    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0 # default value # hidden attribute from object, private

    def get_description(self):
        """summary of the car details , usually you have return statement"""
        print(f"Details of the car\n\tMake/model/year: {self.__make.title()}/{self.__model.upper()}/{self.__year}")

    def get_odometer(self):
        return f'Current milage : {self.__odometer_reading}'

    def set_odometer(self, milage):
        """Updates the odometer reading to given milage"""
        print('Updating the odometer reading ...')
        if milage > self.__odometer_reading:
            self.__odometer_reading = milage
        else:
            print(f'Invalid milage was entered for the odometer! Value entered: {milage}')

    def increment_odometer(self, miles:int):
        """Adds trip miles to your overall milage of the car."""
        print(f'Adding {miles} miles to your odometer reading...')
        # self.__odometer_reading = self.__odometer_reading + miles
        if miles > 0:
            self.__odometer_reading += miles
        else:
            print(f'Miles should be positive number.Value entered :{miles}')



# Create the object (instance of Vehicle class)
car1 = Vehicle('mazda', '6', 2016)
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




