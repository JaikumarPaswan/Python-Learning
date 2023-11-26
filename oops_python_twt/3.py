#Inheritence
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("If p.speak is typed, this will get print")

class Cat(Pet):        #Cat-->child class, Pet-->Parent Class
    def __init__(self, name, age, color):
        super().__init__(name, age)  #super() is parent class-->Pet
        self.color = color

    def speak(self):
        print("Meow")    

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")   
    

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass        

p = Pet("Tim", 19)
#p.show()
p.speak()
c = Cat("Bill", 34, "Brown")
#c.speak()
c.show()
d = Dog("Jill", 25)    
d.speak()    
f = Fish("bubble", 12)
f.speak()     #Here the parrent class speak will get print as child class do not have a speak input
