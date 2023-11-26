myDict = { 
     "Fast": "In a Quicker Manner",
     "Harry": "A Coder",
     "Marks": [1,2,5],
     "anotherdict":{'virat': 'Something Bigger in Size'},
     1:2
}

#Dictionary Methods
print(list(myDict.keys())) #Prints the keys of the dictionary #list is type casted here but there is no need to typecast
print(myDict.keys())

print(myDict.values()) #Prints the values of the dictionary
print(myDict.items()) #Prints the (key, value) for all contents of the dictionary

updateDict = {
     "ball": "An round object to play",
     "biscuit": "Made of wheat or any other flour by baking"
}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updateDict

print(myDict.get("Harry"))#Prints value associated wih "Harry"
print(myDict["Harry"])#Prints value associated wih "Harry" BUT(see down)

#Difference between .get and [] syntax in Dictioanaries
print(myDict.get("Harry2")) #Returns None as Harry2 is not present in the dictionary
#print(myDict["Harry2"]) #throws an error as Harry2 is not present in dictionary

print(myDict.keys())
print(myDict['anotherdict']['virat'])