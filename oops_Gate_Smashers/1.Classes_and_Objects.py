class employee:
    def putdata(self):         #method/function
        self.id = int(input("Enter employee id "))   #instance variabes/data/property/attribute (instance variable  is unique to each object and is therefore an instance variable. )
        self.name = input("Enter employee name ")
        self.salary = float(input("Enter employee salary "))

    def display(self):
        print("Employee id:",self.id)
        print("Employee name:",self.name)
        print("Employee saary:",self.salary)

a = employee()     #object
a.putdata()
a.display()





