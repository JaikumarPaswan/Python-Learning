class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") #This will run as soon as the object is created, Constructor is a unique function which runs automatically when an object is created of a class
                                      # Main function is to initialize or assign values to the data members of that class.
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")
  
    
    @staticmethod
    def greet():
        print("Good Morning, Sir")


harry = Employee("Harry", 100, "Youtube")
# harry = Employee() --->This will throw an error
harry.getDetails()
