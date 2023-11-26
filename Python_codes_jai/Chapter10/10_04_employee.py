class Employee:
    company = "Google"

harry = Employee() #object
jai = Employee()

harry.salary = 300 #Instance(object) attribute
jai.salary = 400

print(harry.company)
print(jai.company)

Employee.company = "Youtube"  #can change the class attribute

print(harry.company)
print(jai.company)
print(harry.salary)
print(jai.salary)

jai.company = "Instagram" #Instance(object) attribute 
print(jai.company)
