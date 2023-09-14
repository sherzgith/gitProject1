# Chapter 10: Exception handling
# below syntax for try/except/finally
# try:
#     # code to execute
# except CertainError as variableToSaveATextOfError:
#     # steps to handle exception, message to print
import  time
from src.o_o_programming.car_class import *
car1 = Car('mazda', '6', 2016)
try:
    car1.get_description()
    print(sum1) # raises NameError
    print(f'new exception : {11 / 0}')  # raises ZeroDivisionError
    print('car1.odometer_reading: ', car1.__odometer_reading) # raises AttributeError
    print('We should not be seeing this***********')

except (ZeroDivisionError, AttributeError) as error:
    print('Attribute or ZeroDivision ERROR was caught ...')
    print(f'Body of the message : {error} ')
except NameError as error:
    print(f"ERROR: Name error happened : {error}")
except TimeoutError:
    time.sleep(10)
finally:
    print('This is the FINALLY block, executes regardless of any exception')


print('---------------------------')
print(car1.get_odometer())
car1.set_odometer(10000)
print(car1.get_odometer())
