# #string formatting (python3)
# name = "Jai"
# age = 18
# #print("hello {} your age is {}".format(name, age))


# #python(3.6)
# print(f"hello {name} your age is {age}")

# print(f"hello {name} your age is {age + 2}")  #you can also do calculations


# #Exercise 

# num1, num2, num3 = input("enter three numbers comma seperated:").split(",")
# print(f"average of three numbers: {(int(num1) + int(num2) + int(num3)) / 3}")

# #string indexing

# language = "python"

# print(language[2])
# print(language[-2])

#string slicing
#syntax- [start argument : stopargument-1]

lang="python"

print(lang[2:5])
print(lang[-3:4])

#step argument

print(lang[0:4:2])
print(lang[0::2])
print(lang[0:4:1])
print(lang[5::-1])

#reverse order name
name = input("Enter name")
print(f"reverse order of your name is {name[-1::-1]}")
