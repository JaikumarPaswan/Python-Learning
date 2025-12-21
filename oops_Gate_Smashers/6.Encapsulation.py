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


#Public Access Modifier:
#The members of a class that are declared public are easily 
# accessible from any part of the program. All data members 
# and member functions of a class are public by default. 

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