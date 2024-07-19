## https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/  - oops
## https://towardsdatascience.com/python-decorators-in-oop-3189c526ead6#:~:text=Decorators%20are%20functions%20(or%20classes,and%20then%20returns%20a%20percentage.
## https://www.analyticsvidhya.com/blog/2024/01/exception-handling-in-python/  -exception handling basic
## https://www.linkedin.com/pulse/custom-exceptions-learn-how-create-your-handle-errors-h-s-karthik/  - custom exception handling



## OOPS
'''
Class
Object
Method
Inheritance
Class Constructor
Polymorphism
Data Abstraction
Encapsulation
Dynamic Binding
Message Passing 
'''

'''
This code implements 
class
obect
Inheritance
class constructor
polymorphism
Dynamic binding
'''

class Car:
    def __init__(self,name,mileage):  ## constructor
        # self.name = name    # normal way of using class member
        # self._name = name   ## This is to understand that the variable is protected- _name
                              ## this is just a way of understand that the scope of this variable should be kept protected.
                              ## but actually the adding _ at the start doesn't intrinsically make it projected and is accessible publically.

        self.__name = name   # This is intrinsically private. For Debugging purpose can be accessed only via ( _class_name.__name )
        self.mileage = mileage

    def description(self):
        return f"The {self.__name} car gives the mileage of {self.mileage} km/l"

    def start_engine(self): 
        raise NotImplementedError("Subclass must implement this method")

class Audi(Car):    #child class
  def description(self):                                        #Polymorphism
    print("This the description function of class AUDI.")

  def start_engine(self):
    return "The Audi engine has started."

class BMW(Car):    #child class
  def description(self):                                        #Polymorphism
    print("This the description function of class BMW.")

  def start_engine(self):
    return "The BMW engine has started."

def start_car_engine(car):                                      #Dynamic binding 
    print(car.start_engine())




print(' ------------Normal calling functions -----------')
obj1 = BMW("BMW 7-series",39.53)
print(obj1.description())

obj2 = Audi("Audi A8 L",14)
print(obj2.description())



print(' ------------Test Private member variables call -----------')
obj = Car("BMW 7-series",39.53)
#accessing private variable via class method 
print(obj.description())
#accessing private variable directly from outside
print(obj.mileage)
print(obj._Car__name) 


print('-------------Dynamic binding test -----------------')
audi_car = Audi()
bmw_car = BMW()
start_car_engine(audi_car)           # dynamic binding (based on which car object passed the function behaves accordingly )         
start_car_engine(bmw_car)            # Output: The bmw engine has started.