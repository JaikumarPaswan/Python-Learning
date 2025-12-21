#Interface is nothing but abstract class which contains only 
# abstract method and not any normal method

from abc import ABC, abstractmethod

class AnimalInterface(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(AnimalInterface):
    
    def make_sound(self):
        print("Woof woof!")
    
    def move(self):
        print("The dog is running.")

class Bird(AnimalInterface):
    
    def make_sound(self):
        print("Tweet tweet!")
    
    def move(self):
        print("The bird is flying.")

# Instantiate the classes
dog = Dog()
dog.make_sound()  # Outputs: Woof woof!
dog.move()        # Outputs: The dog is running.


#Benefits of Using Interfaces
#Encapsulation of Common Behavior: Interfaces encapsulate behavior that must be implemented by multiple classes.
#Consistency: Ensures that all implementing classes follow the same method signatures.
#Flexibility: Allows different classes to be used interchangeably if they implement the same interface.
#Separation of Concerns: Promotes separation of interface and implementation.