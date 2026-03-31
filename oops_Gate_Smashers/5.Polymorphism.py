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


# Polymorphism means same interface with different behavior.
# In Python, it is mainly achieved using method overriding, duck typing, and operator overloading.
# Python does not support true compile-time polymorphism, but it can be simulated using default arguments.


# Duck typing in Python is a concept where the type of an object is not checked explicitly. Instead, Python focuses on whether the object has the required methods or behavior.

# It follows the idea:
# “If it behaves like a duck, it is treated as a duck.”

# For example, if different objects have a speak() method, Python will allow them to be used interchangeably, regardless of their class.

# Short version (if interviewer wants quick answer):
# Duck typing means Python determines an object’s suitability based on its behavior (methods), not its type.




# 🔵 Compile-Time Polymorphism (Static)
# Function Overloading (simulated using default arguments)

# 🔴 Run-Time Polymorphism (Dynamic)
# Method Overriding
# Operator Overloading
# Duck Typing
# Function Polymorphism (like len())




# 🔵 Compile-Time Polymorphism (Simulated Overloading)
# def add(a, b, c=0):
#     return a + b + c

# print(add(2,3))     # 5
# print(add(2,3,4))   # 9

# Same function name handles different number of arguments.
# Python doesn’t support true overloading, so we use default arguments to simulate it.
# Decision happens before execution (conceptually compile-time).



# 🔴 Method Overriding (Run-Time)
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# B().show()   # B

# Child class provides its own implementation of a parent method.
# Which method runs depends on the object created.
# Decision is made at runtime.



# 🔴 Operator Overloading

# print(2 + 3)        # 5
# print("a" + "b")    # ab

# Same operator (+) behaves differently for different data types.
# It performs addition for numbers and concatenation for strings.
# This is built-in polymorphism in Python.



# 🔴 Duck Typing
# class Dog:
#     def speak(self):
#         print("Bark")

# def call(obj):
#     obj.speak()

# call(Dog())   # Bark

# Python checks behavior (methods), not the object type.
# Any object with a speak() method will work here.
# This makes Python flexible and dynamic.



# 🔴 Function Polymorphism
# print(len("hello"))   # 5
# print(len([1,2,3]))   # 3
# Same function works with different data types.
# len() calculates length for strings, lists, etc.
# Behavior changes based on input type.