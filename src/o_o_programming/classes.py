# Chapter 9

class Dog:
    # state/attributes
    # execute automatically by python when class is instantiated ( when object is created)
    def __int__(self, name, breed, age, color):

        self.breed = breed
        self.age = age
        self.name = name
        self.color = color
    # behaviour
    # self keyword is used to show that functions and variables belong to class
    def bark(self):
        print('Dog is barking')

    def run(self):
        print(f'{self.name} is running fast......')



# creating the object from the class (model)
# creating the instances from the class - INSTANTIATION

dog1 = Dog()
dog1.name = 'Roxi'
print(f'The name of the dog1 is {dog1.name.upper()}')

dog2 = Dog()
dog2.name = 'Rex'
print(f'The name of the dog2 is {dog2.name.upper()}')

dog3 = Dog()
dog3.name = 'Rooney'
print(f'The name of the dog3 is {dog3.name.upper()}')


print('Behaviours of dogs: Dogs are running  ')

dog1.run()
dog2.run()
dog3.run()





