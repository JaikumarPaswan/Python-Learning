s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)  #s2 is substring of s1
print(s2 not in s1)

#String Concatination
s1 = "geeks"
s2 = "forgeeks"
s3 = s1+s2
s4 = "Welcome to " + s1 + s2

print(s3)
print(s4)


#Position of substring 
print("!''Position of substring''!")
s1 = "geeksforgeeks"
s2 = "geeks"

print(s1.index(s2))  #returns starting positin of substring
print(s1.index('s')) #⭐p.s:- use find() instead of index,because, if substring is not present, index will provide error while find will return -1

print(s1.rindex(s2)) #Checks list from end and return starting position of substring

print(s1.index(s2,1,13)) #checks list from postion 1-13 and return starting position of string
#if substing is not present in string then it will raise error


#More sting operations
print("!''More sting operations''!--1")
s1 = "geeks"
print(len(s1))

s2 = s1.upper()
print(s2)

s3 = s2.lower()
print(s3)

print(s1.islower())
print(s2.isupper())


#More sting operations
print("!''More sting operations''!--2")
s = "GeeksforGeeks Python Course"

print(s.startswith("Geeks"))
print(s.endswith("urse"))
print(s.startswith("eeks", 1)) #starts seaarching from 1st index 
print(s.startswith("Geeks", 8, len(s)))


#⭐ split() method
print("!''⭐ split()  and join() method''!--3")
s1 = "geeks for geeks"
print(s1.split())  #It will split the string by 'white-space' or \'n' by default as a separate

s2 = "geeks,for,geeks"
print(s2.split(",")) #here we have placed ',' as a separator

#⭐ join() method
l = ['geeks', 'for', 'geeks']
print(" ".join(l))
print(",".join(l))


# strip() method
print("!''strip() method''!--4")
s = "--geeksforgeeks---"
print(s.strip("-")) #It will romove provided parameter from the ends only, if any parameter is not rpovided it will remove the white-spaces
print(s.lstrip("-")) #left-strip
print(s.rstrip("-")) #right-strip


# find() method [better alternatie of index() method]
print("!''index method''!--5")
s1 = "geeks for geeks"
s2 = "geeks"

print(s1.find(s2))
print(s1.find("gfg"))
print(s1.find(s2,1,len(s1)))