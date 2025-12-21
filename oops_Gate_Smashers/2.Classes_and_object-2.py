class student:
    def __init__(self, my_roll, my_name, my_marks):
        self.rollno = my_roll
        self.name = my_name
        self.marks = my_marks

    def average(self):
        return sum(self.marks)/len(self.marks)
        
first_student = student(1,'jai', [85,74,70,68])
print(first_student.name)
print(first_student.average())








#The __init__ method in Python is a special method that is automatically called when a new instance of a class is created.

#__init__: Used to initialize a newly created object. It's typically used to set initial values for instance attributes.
#Regular Methods: Used to define the behavior of an object and can be called on an instance to perform operations.
 