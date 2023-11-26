l1 = [14,1,5,34,65,3,4]
print(l1)
#l1_sorted = l1.sort() -->This is wrong, original list l1 is sorted using l1.sort method
#print(l1_sorted)

l1.sort() #sorts the list
print(l1)

l1.reverse() #reverses the list
print(l1) #updated list l1 is reversed

l1.append(45) #adds 45 at the end of the list 
l1.insert(2,544) #inserts 544 at index 2
l1.pop(2) #removes element at index 2
l1.remove(34) #removes 34 from the list
print(l1)

