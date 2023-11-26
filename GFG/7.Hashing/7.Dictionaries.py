#Collection of key-value Pairs
#Unordered
#Mutable  (only tuples are immutable)
#All keys must be distinct
#Values may be repeated
#Uses hashing internelly

#You can access values using keys in dictionaries as index

d={}

d["laptop"]=40000
d["mobile"]=15000
d["earphone"]=1000

print(d)
print(d["mobile"])  #If key not present, it will give error

print("-----------------------")


d = {110:"abc", 101:"xyz", 105:"pqr"}

print(d.get(101))

print(d.get(125))      #If key not present, it will not give error
print(d.get(125,"NA")) #If key not present, we can print our statement
#    ↓
if 125 in d:
    print(d[125])
else:
    print("NA")


print("-----------------------")


d={110:"abc", 101:"xyz", 105:"pqr", 106:"bcd"}

print(d)

d[101] = "xox"
print(d)

print(len(d))

#pop will delete the key-value and  print the deleted value of key value
print(d.pop(105))
print(d)

del d[106]
print(d)

d[108] = "cde"

#deletes the last inserted key-value pair
print(d.popitem(1))