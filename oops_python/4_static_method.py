class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")


jai = Employee()
jai.salary = 100000
jai.getSalary("Thanks!") #This is equals to Employee.getSalary(jai)
jai.greet() #Employee.greet()
jai.time()
