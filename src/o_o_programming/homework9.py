

#  9-1, 9-4
class Restaurant:

    def __init__(self, name, cuisine_type):

        self.name = name
        self.cuisine_type = cuisine_type
        self.__number_served = 0
    def open_restaurant(self):
        print(f"{self.name} is Open now!")

    def describe_restaurant(self):
        print(f"{self.name} is fine {self.cuisine_type} restaurant.")



    def get_customers_served(self):
        return f"The {self.name} restaurant served {self.__number_served} customers so far."

    def set_number_served(self, customer):
        print(f"Setting the number to {customer}.")
        self.__number_served = customer


    def increment_number_served(self, customer:int):
        """ Adds more customers to the current number_served"""
        print(f"Incrementing  the number served by  {customer}.")
        if customer > 0:
            self.__number_served += customer
        elif customer == 0:
            print(f"You added zero , its not acceptable!")
        else:
            print(f'Number of customers should be positive number.Value entered :{customer}')
        print(f"Current number of Customers served : {self.__number_served}")









restaurant1 = Restaurant('Sulk Road', 'Uzbek')
print(restaurant1.get_customers_served())
restaurant1.set_number_served(10)
print(restaurant1.get_customers_served())
restaurant1.increment_number_served(2)
restaurant1.increment_number_served(-1)
restaurant1.increment_number_served(0)




