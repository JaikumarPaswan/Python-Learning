class employee:
    def __init__(self):         #constructor '__init__' method (It initializes the method automatically without calling it)  #A Python class can only have one __init__ function defined at a time. If multiple __init__ methods are defined within a single class, the latest one in the code will override all the previous definitions, and only that last definition will be used when an object is instantiated
        self.id = int(input("Enter employee id "))   #instance variabes/data/property/attribute (instance variable  is unique to each object and is therefore an instance variable. )
        self.name = input("Enter employee name ")
        self.salary = float(input("Enter employee salary "))

    def display(self):
        print("Employee id:",self.id)
        print("Employee name:",self.name)
        print("Employee saary:",self.salary)

a = employee()     #object1
b = employee()     #object2
a.display()
b.display()

