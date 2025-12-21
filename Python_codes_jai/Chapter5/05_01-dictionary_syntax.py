myDict = { 
     "Fast": "In a Quicker Manner",
     "Harry": "A Coder",
     "Marks": [1,2,5],
     "anotherdict":{'virat': 'Something Bigger in Size'},
     2 : 3,
     2 : 3  #duplicates are not shown, only one instance of similar key-value pairs are stored
}

print(myDict['Fast'])
print(myDict['Harry'])

myDict['Marks'] = 45 #Dictionaries are Mutable(can be changed)
print(myDict['Marks'])

print(myDict['anotherdict']['virat'])

print(myDict.keys())

print(list(myDict.keys())[-2:])