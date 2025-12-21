#This code demonstrates the concept of Python oops inheritance 
# and method overriding in Python classes. It shows how 
# subclasses can override methods defined in their parent
# class to provide specific behavior while still inheriting
# other methods from the parent class. 
#Method overriding, ⭐ Run time polymorphism

class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()




#In object oriented Programming Python, Polymorphism simply 
#means having many forms. For example, we need to determine 
#if the given species of birds fly or not, using polymorphism 
#we can do this using a single function.

#We can achieve polymorphism using 4 ways:
#1. Duck Typing
#2. Method Overloading
#3. Operator overloading
#4. Method overriding


#Operator overloading,⭐ Compile time Polymorphism
#Eg:- 

# print(1+2)
# print("1" + "2")


