#Python by default do not suport Abstract Classes 

# i)A class that contains one or more abstract methods is called 
#  an abstract class.
# ii)An abstract method is a method that has a declaration but 
#  does not have an defination/implementation.
# iii)Object of an abstract class cannot be created 
#  (i.e that class cannot be instantiated)
# iv) Python provides abc module to work with abstraction

# v)It is used to define a common interface for its subclasses. 
#  Abstract classes are typically used to define a template 
#  for other classes and can contain both abstract methods 
#  (which must be implemented by subclasses) and concrete methods 
#  (which have an implementation in the abstract class). 

# vi)⭐Subclasses of the abstract class are required to 
#  implement all abstract methods.

# vii)⭐Promotes Code Reusability, Encapsulation of Common Behavior,
#  Establishes a common interface/template that all subclasses must adhere to.


from  abc import ABC, abstractmethod

class Car(ABC):  #even if we dont write ABC here, it will work
    def wheel(self):
        print("Every car has 4 wheels")

    @abstractmethod   #this provides a common template for child-classes
    def speed(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Maruti(Car):
    def speed(self):
        print("maruti speed is 120 km/hr")

    def color(self):
        print("--Red--")

class TATA(Car):
    def speed(self):
        print("TATA speed is 100 km/hr")

    def color(self):
        print("--Blue--")

    def fueltype(self):
        print("E20")

maruti = Maruti()
maruti.wheel() 
maruti.speed() #⭐All abstract methods needs to be implemented otherwise we will get error output 
maruti.color()


tata = TATA()
tata.wheel()
tata.speed()
tata.color()
tata.fueltype()






# @abstractmethod:
# Doesn’t hide data directly ❌
# Forces a common interface ✔
# Helps hide how things are done ✔

# 🧠 One-line answer (interview)
# @abstractmethod doesn’t directly hide data, but it helps achieve abstraction 
# by defining a method without implementation, so users only see what to use, 
# not how it works.