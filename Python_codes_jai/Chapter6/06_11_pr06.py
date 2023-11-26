marks = int(input("Enter Your Marks\n"))

if (marks>=90):   #If can be executed without brackets also
    grade = "EX"
elif(marks>=80):
    grade = "A"
elif(marks>=70):
    grade = "B"    
elif(marks>=60):
    grade = "C"
elif(marks>=50):
    grade = "D"
else:
    grade = "f"

print("Your grade is: " + grade)