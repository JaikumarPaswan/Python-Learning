#Escape Sequence
 #i)
# s = 'welcome to Geek's Course' #Invalid Syntax

s = 'welcome to Geeks\'s Course' #Corrected program
print(s)

#ii)
s = "Hii, \nWelcome to the Course"
print(s)

#iii)
s1 = "A simple \ example"
s2 = "Backlash at the end \\" # \" is used to escape double quote thats why \\ is used
s3 = "\\n"
s4 = "\\t"


print(s1)
print(s2)
print(s3)
print(s4)



#Raw Strings

s1 = "C:\project\name.py"

s2 = r"C:\project\name.py"

print(s1)
print(s2)