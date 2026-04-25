
# #create a list using []
# a = [1,2,4,56,6]

# #print the list using print
# print(a[3])

# #Access using index using a[0], a[1], a[2]
# print(a[2])

# #change the value of list using 
# a[0] = 98
# print(a)

# #We can create a list using items of different type
# b = [45, "jai", False, 3.2]
# print(b)

# #List slicing
# friends = ["jai", "raj", "anushk", "omkar", 45]
# print(friends[0:3])
# print(friends[-4:])


# #list_methods
# l1 = [1,65,43,7,8,32,41]
# print(l1)
# l1.sort() #sort the list
# print(l1)
# #⭐ Sort in reverse
# l1.sort(reverse=True)
# print(l1)
# l1[4] = 98 #changing a value in list
# print(l1)

#⭐sort array according to second element of pair
arr=[(12,3), (4,7), (2,8), (11,4)]
arr.sort(key=lambda x:x[1])
print(arr)

# print(l1.reverse())
# print(l1)
# l1.reverse() #reverse the list
# print(l1)
# l1.append(93) #adds at the end of the list
# print(l1)
# l1.insert(0,544) #inserts 544 at 0th index  of list
# print(l1)
# l1.pop(2) #removes index element of the list
# print(l1)
# l1.remove(32) #removes 43 from the list
# print(l1)

# #copy of list
# l2 = l1.copy()
# print(l2)
# l2.reverse()
# print(l2)

#Tuples

#creating a tuple using ()
t = (1,2,4,5,1,1,1)

print(t)

#Printing the elements of a tuple
print(t[0])

print(t.count(1)) #counts number of element

print(t.index(5)) #tells index number

t1 = (1) #wrong way to declare a tuple with single element
print(t1)
t2 = (1,)#Right way to declare a tuple with single element
print(t2)

# *Cannot update the values of a tuple

#



