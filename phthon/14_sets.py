a = {1,3,4,5,1}  #set is a collection of non-repetitive elements
print(type(a))
print(a)

#Important:This syntax will create an empty
#        dictionary and not an empty set
a = {}
print(type(a))


#An empty set
b = set()
print(type(b))
b.add(4)
b.add(5)
b.add(12)
b.add(34)
b.add(26)
b.add((8,5,6))

print(b)

#Length of a set
print(len(b))

b.remove(5)

print(b)





