class Employee:
    company = "Google"
    salary = 100 #class attribute

jai = Employee()
rajni = Employee()
#jai.salary = 300 #instance attribute or instance variable
#rajni.salary = 400

print(jai.company)
print(rajni.company)
Employee.company = "YouTube"
print(jai.company)
print(rajni.company)
jai.salary = 45  #instance attribute or instance variable
print(jai.salary)
print(rajni.salary)





