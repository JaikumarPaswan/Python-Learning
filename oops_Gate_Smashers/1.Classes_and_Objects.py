class employee:
    def putdata(self):         #method/function
        self.id = int(input("Enter employee id "))   #instance variabes/data/property/attribute (instance variable  is unique to each object and is therefore an instance variable. )
        self.name = input("Enter employee name ")
        self.salary = float(input("Enter employee salary "))

    def display(self):
        print("Employee id:",self.id)
        print("Employee name:",self.name)
        print("Employee saary:",self.salary)

a = employee()     #object/instance
a.putdata()
a.display()





#Whenever we create an object from a class, 'self' refers to the current object instance. It is essential for accessing attributes and methods within the class.