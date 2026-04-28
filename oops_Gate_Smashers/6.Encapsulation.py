# Encapsulation is the bundling of data (attributes) and methods (functions) 
# within a class, restricting access to some components to control interactions. 
# A class is an example of encapsulation as it encapsulates all the data that 
# is member functions, variables, etc.

#Jennys lecture

# Encapsulation is one of the fundamental concepts in object-oriented 
# programming (OOP). It describes the idea of wrapping data 
# and the methods that work on data within one unit. This puts
# restrictions on accessing variables and methods directly and 
# can prevent the accidental modification of data. To prevent 
# accidental change, an object’s variable can only be changed 
# by an object’s method. Those types of variables are known as 
# private variables.

# A class is an example of encapsulation as it encapsulates 
# all the data that is member functions, variables, etc. 
# The goal of information hiding is to ensure that an object’s 
# state is always valid by controlling access to attributes 
# that are hidden from the outside world.

class Student:
    def __init__(self, name, rollno, age):
        self.name = name  #public instance variable
        self._rollno = rollno #protected instance variable
        self.__age = age #private instance variable

    def get_age(self):  #By using getter method, we can access private variable
        return self.__age
    
    def set_age(self, age):  #By using setter method, we can set/modify private variable
        self.__age = age

s1 = Student("Jai", 35, 21)
print(s1.get_age())

s1.set_age(25)
print(s1.get_age())

# 🎯 Encapsulation in Python

# Encapsulation is the concept of bundling data (variables) and methods together 
# inside a class and restricting direct access to the data.

# It is used for:
# Data hiding
# Protecting data
# Controlling access
# 🔑 How it is achieved in Python

# Using access modifiers:
# Public → x
# Protected → _x
# Private → __x

#Public Access Modifier:
#The members of a class that are declared public are easily 
# accessible from any part of the program. All data members 
# and member functions of a class are public by default. 
# Eg. A class can access the variable of another Class

# class Class1:
#     def __init__(self):
#         self.x = 10
#         self.y = 20

# class Class2:
#     def __init__(self):
#         self.obj = Class1()

#     def show(self):
#         print(self.obj.x)
#         print(self.obj.y)

# c = Class2()
# c.show()   #10 20



#Protected Access Modifier:
#The members of a class that are declared protected are only 
# accessible to a class derived from it. Data members of a 
# class are declared protected by adding a single underscore
#  ‘_’ symbol before the data member of that class. 

#Private Access Modifier
# The members of a class that are declared private are accessible 
# within the class only, private access modifier is the most 
# secure access modifier. Data members of a class are declared 
# private by adding a double underscore ‘__’ symbol before the 
# data member of that class. 









# 🔵 Encapsulation

# Encapsulation means bundling data (variables) and methods together and controlling access to them.

# It helps in data hiding
# Protects data from unauthorized access
# Achieved using access modifiers
# 🔑 Access Modifiers in Python

# Python does not have strict access control like Java/C++, but it uses naming conventions.

# 🟢 1. Public
# Accessible from anywhere
# No restriction
# class A:
#     def __init__(self):
#         self.x = 10   # public

# obj = A()
# print(obj.x)   # ✅ accessible



# 🟡 2. Protected
# Meant to be used within class and subclasses
# Prefix: _
# class A:
#     def __init__(self):
#         self._y = 20   # protected

# class B(A):
#     def show(self):
#         print(self._y)

# obj = B()
# obj.show()   # ✅ accessible

# 👉 Still accessible outside, but should not be used directly



# 🔴 3. Private
# Accessible only inside the class
# Prefix: __ (double underscore)
# class A:
#     def __init__(self):
#         self.__z = 30   # private

#     def show(self):
#         print(self.__z)

# obj = A()
# obj.show()     # ✅ works
# # print(obj.__z) ❌ Error
# 🔍 How Python handles private
# print(obj._A__z)   # accessing private (name mangling)

# 👉 Python internally changes:
# __z → _ClassName__z



# ⚖️ Summary
# Type	Syntax	Access
# Public	x	Anywhere
# Protected	_x	Class + subclass
# Private	__x	Only class
# 🧠 One-line takeaway

# Encapsulation hides data and controls access using public, protected, and private members.

# 🎯 Interview Tip
# Say: Python doesn’t enforce strict access control, but uses naming conventions (_, __) to indicate access levels.