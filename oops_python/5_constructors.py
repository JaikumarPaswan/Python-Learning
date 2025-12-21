class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):   #A Python class can only have one __init__ function defined at a time. If multiple __init__ methods are defined within a single class, the latest one in the code will override all the previous definitions, and only that last definition will be used when an object is instantiated
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

jai = Employee("jai", 100, "YouTube")
jai.getDetails()  #instance.function()



#The __init__ method in Python is a special method that is automatically called when a new instance of a class is created.

#__init__: Used to initialize a newly created object. It's typically used to set initial values for instance attributes.
#Regular Methods: Used to define the behavior of an object and can be called on an instance to perform operations.
