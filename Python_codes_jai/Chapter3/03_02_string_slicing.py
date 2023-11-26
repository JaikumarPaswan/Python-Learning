greeting = "Good Morning, "
name = "jaikumar"
#Concatenating two strings
# c = greeting + name
# print(c)

#Accessing Index of String
# print(name[0])
# print(name[1])
# print(name[2])

# #name[2] = "d" #--> Does not work

# #String Slicing
print(name[1:4])
# print(name[:4]) #is same as name[0:4]
# print(name[0:]) #is same as name[0:8]

#Negative Indices
print(name[-8:8]) 
print(name[-7:])
print(name[-5:-2])  
# print(name[-2:-5])  #No Value

#Slicing with Skip value
print(name[0:8:2])  #Third argument decide the value of skip

#Reverse a string
print(name[::-1])


