# Chapter 9

class Dog:
    # state/attributes
    # execute automatically by python when class is instantiated ( when object is created)
    def __init__(self, name, breed, age, color):
        self.breed = breed
        self.age = age
        self.name = name
        self.color = color

    # behaviour
    # self keyword is used to show that functions and variables belong to class
    def bark(self):
        print(f'{self.name.title()} is barking')

    def run(self):
        print(f'{self.name.title()} is running fast......')


dog1 = Dog('rex', 'husky', 5, 'brown')
dog2 = Dog('roxy', 'bulldog', 2, 'white')
my_dog = Dog('puma', 'german shepherd', 3, 'black')

# creating the object from the class (model)
# creating the instances from the class - INSTANTIATION

# dog1 = Dog()
# dog1.name = 'Roxi'
# print(f'The name of the dog1 is {dog1.name.upper()}')
#
# # dog4 = Dog()
# dog4.name = 'Rex'
# print(f'The name of the dog2 is {dog2.name.upper()}')
#
# # dog5 = Dog()
# dog5.name = 'Rooney'
# print(f'The name of the dog3 is {dog3.name.upper()}')


print('Behaviours of dogs: Dogs are running  ')

dog1.run()
dog2.run()
my_dog.run()
dog1.bark()
# print(f"My dog's name is {my_dog.name}"
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
my_dog.run()


class Cat():
    """A simple attempt to model a cat."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_cat = Cat('willie', 6)
your_cat = Cat('larry', 5)
print("My cat's name is " + my_cat.name.title() + ".")
print(f"Your cat's name is {your_cat.name.title()}.")
print("My cat is " + str(my_cat.age) + " years old.")
your_cat.sit()
my_cat.sit()
my_cat.roll_over()
your_cat.roll_over()
