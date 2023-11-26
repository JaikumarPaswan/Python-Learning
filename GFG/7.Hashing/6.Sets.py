#Distinct elements
#Mutable
#Unorded
#No Indexing
#Union, intersection, Set Difference, etc are fast.
#Uses hashing Internally

s1={10,20,30}
print(s1)

#Create set from different data-structure
s2=set([20,30,40])
print(s2)

#This creates an empty dictionary
s3={}
print(type(s3))

#This creates an empty set
s4=set()
print(type(s4))
print(s4)


print("-----------------------")


s={10,20}

s.add(30)
print(s)

s.add(30)
print(s)

#Using update we can add items from other collections/data-structure
s.update([40,50])
print(s)

s.update({60,70}, [80,90])
print(s)


print("-----------------------")


s={10,20,30,40}

#It does not provides an error if item is not present in set which we are trying to discard
s.discard(30)
print(s)

#It will give error if item is not present which we are trying to remove
s.remove(20) #Can be used like:- for x in s remove(x) #this will first check, then only remove
print(s)

#To empty an set
s.clear()
print(s)

#to delete the whole object
s.add(50)
del s

print("-----------------------")


s={10,30,20,40}

print(len(s))
print(20 in s)
print(50 in s)


print("-----------------------")


s1={2,4,6,8}
s2={3,6,9}

#Union
print(s1|s2)
print(s1.union(s2))

#Intersection
print(s1&s2)
print(s1.intersection(s2))

#Difference
print(s1-s2)
print(s1.difference(s2))

#symmetric diffenence
print(s1^s2)
print(s1.symmetric_difference(s2))


print("-----------------------")


s1 = {2,4,6,8}
s2={4,8}

#Disjoint
print(s1.isdisjoint(s2))

#issubset
print(s1<=s2)
print(s1.issubset(s2))

#ispropersubset
print(s1<s2)

#superset
print(s1.issuperset(s2))
print(s1>=s2)

#propersuperset
print(s1>s2)