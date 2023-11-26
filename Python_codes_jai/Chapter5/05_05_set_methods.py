#Creating an empty set
b = set()
print(type(b))

#Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) #Adding a value repeatedly does not change a set
b.add((5,6,7))

#b.add({4:5}) Cannot add list or dictionary to sets
print(b)

#Length of the set
print(len(b)) #Prints the length of this set
print(b)

#Removoval of an item
b.remove(5) #removes 5 from set b
#b.remove(15) #throws an error while trying to remove 15(as 15 is notpresent in the set)
print(b)

print(b.pop()) #randomly remove a object in the set

print(b)
print(b)