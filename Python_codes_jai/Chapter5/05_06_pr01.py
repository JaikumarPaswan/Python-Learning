myDict ={
    "pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("Options are ", myDict.keys())
a = input("Enter the Hindi word\n")
#print("The meaning of your word is :", myDict[a])

#Below line will not throw an error if the keyvalue is not present in the dictionary
print("The meaning of your word is:", myDict.get(a))