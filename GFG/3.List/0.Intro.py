l = [10, 20, 30, 40, 50]

print(l)
print(l[0:5])
print(l[-1])

#append
l.append(30)
print(l)

#insert
l.insert(1, 15)
print(l)

print(15 in l)

print(l.count(30))

print(l.index(30)) # returns first index where 30 appears

print(l.index(30, 4, 7)) # returns index of 30 between index 4 and 6(7-1)

print("----remove()----")
l.remove(20)
print(l)

print("pop")
print(l.pop()) # pop also displays the value which get popped
               # pop only used to remove one value, or the last value, 
               # where del can be used to remove one value and many[0:2...]
print(l.pop(2)) # pop by index

print(l)

print("del") # del can be used to delete one as well as many value 
del l[1]
print(l)

del l[0:2]
print(l)

l1 =[10, 40, 20, 50]

print(l1)

print("max")
print(max(l1))

print("reverse")
l1.reverse()
print(l1)

print("sort")
l1.sort
print(l1)


# -----Reverse-----
l = [10, 20, 30, 40, 50]
print(l)

print(l[0:5:2])

print(l[1:4])
print(l[4:1:-1])

print(l[-1:-6:-1]) 
print(l[::-1])


#making an arr with  all elements -1
arr = [-1]*3
print(arr)

arr1 = [-1 for x in range(3)]
print(arr1)