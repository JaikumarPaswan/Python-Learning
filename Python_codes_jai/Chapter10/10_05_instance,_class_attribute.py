class Employee:
    company = "Google"
    salary = 100

harry = Employee() #object
jai = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300 #class attribute
# jai.salary = 400

harry.salary = 45
print(harry.salary)
print(jai.salary)

# Below line throws an error as adress is not present ininstance/class
# print(jai.address)