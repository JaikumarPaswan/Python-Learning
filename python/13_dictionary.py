myDict = {
    "Fast": "In a quick Manner",
    "Jai": "An Indian Name Means Victory",
    "Marks" : [1,3,4,6],
    "anotherdict": {"virat": "player"},
    "num" : 4
}
# print(myDict["Fast"])
# myDict["Marks"] = [23,46]  #changing key value
print(myDict["Marks"])
# print(myDict["anotherdict"])
# print(myDict["anotherdict"]["virat"])
# # print(myDict.items())  #prints keys, values for all the content of the dictionary

# updateDict={
#     "Lovish" :  "friend"
# }
# myDict.update(updateDict) #update the dictionary by adding key, values
# print(myDict)


# print(myDict.get("Marks"))

# print(myDict["num"])



#1.The most common way to access items serially is using the .items() method, which provides key-value pairs as tuples
# my_dict = {
#     'apple': 1,
#     'banana': 2,
#     'cherry': 3
# }

# for key, value in my_dict.items():
#     print(f"Key: {key}, Value: {value}")



#2.If you only need the values and not the keys, use the .values() method. 
# my_dict = {
#     'apple': 1,
#     'banana': 2,
#     'cherry': 3
# }

# for value in my_dict.value():
#     print(f"Value: {value}")


#3. Iterate through only Keys (.keys()) If you only need the keys, you can use the .keys() method, or simply iterate over the dictionary directly, as looping through a dictionary by default iterates over its keys. python
# my_dict = {
#     'apple': 1,
#     'banana': 2,
#     'cherry': 3
# }

# # Method A: Using .keys()
# for key in my_dict.keys():
#     print(f"Key: {key}")

# # Method B: Direct iteration (more Pythonic)
# for key in my_dict:
#     print(f"Key: {key}")