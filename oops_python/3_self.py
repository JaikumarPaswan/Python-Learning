class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

jai = Employee()
jai.salary = 100000
jai.getSalary() #This is equals to Employee.getSalary(jai)






