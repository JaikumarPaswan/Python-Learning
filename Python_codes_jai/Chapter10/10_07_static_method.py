class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n {signature}")
  
    @staticmethod
    def greet():
        print("Good Morning, Sir")


harry = Employee()
harry.salary = 10000
harry.getSalary("Thanks!")  #This is equal to:- Employee.getSalary(harry)  [use this without self parameter, You will able to identify the error easily]
harry.greet()   #This is equal to:- Employee.greet()
Employee.greet()
