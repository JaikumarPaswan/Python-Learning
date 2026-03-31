# In Python, super() function is used to call methods from a parent (superclass) 
# inside a child (subclass). It allows to extend or override inherited methods 
# while still reusing the parent's functionality.

class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        super().show()   # Calling parent method
        print("This is Child class method")

obj = Child()
obj.show()



# Explanation:

# Parent class has a method show() and child class overrides the same method.
# super().show() calls the parent class method inside the child class.
# This allows the child class to reuse the parent’s functionality and then add 
# its own behavior.


# Why Use super()?
# No need to hardcode parent class names, useful when class hierarchies change.
# Works with single, multiple, and multilevel inheritance.
# Improves code reusability and maintainability.
# Prevents duplicate initialization in complex hierarchies.