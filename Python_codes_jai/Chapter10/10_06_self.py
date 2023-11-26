class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 10000
harry.getSalary()  #This is equal to:- Employee.getSalary(harry)  [use this without self parameter, You will able to identify the error easily]