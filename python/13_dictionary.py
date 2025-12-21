myDict = {
    "Fast": "In a quick Manner",
    "Jai": "An Indian Name Means Victory",
    "Marks" : [1,3,4,6],
    "anotherdict": {"virat": "player"}
}
print(myDict["Fast"])
myDict["Marks"] = [23,46]  #changing key value
print(myDict["Marks"])
print(myDict["anotherdict"])
print(myDict["anotherdict"]["virat"])
# print(myDict.items())  #prints keys, values for all the content of the dictionary

updateDict={
    "Lovish" :  "friend"
}
myDict.update(updateDict) #update the dictionary by adding key, values
print(myDict)


print(myDict.get("Marks"))

