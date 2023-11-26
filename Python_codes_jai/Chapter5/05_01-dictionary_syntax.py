myDict = { 
     "Fast": "In a Quicker Manner",
     "Harry": "A Coder",
     "Marks": [1,2,5],
     "anotherdict":{'virat': 'Something Bigger in Size'}
}

print(myDict['Fast'])
print(myDict['Harry'])

myDict['Marks'] = [45,36] #Dictionaries are Mutable(can be changed)
print(myDict['Marks'])

print(myDict['anotherdict']['virat'])

print(myDict.keys())