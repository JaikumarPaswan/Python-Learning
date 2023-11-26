#This algorithm works by assuming the pivot element as the last element. 
#If any other element is given as a pivot element then swap it first with 
#the last element.

#Pivot is at its correct position but in Hoare's, 
#pivot is not at its correct position

def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i=i+1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[h]=arr[h], arr[i+1]
    return i+1



arr=[10,80,30,90,50,70]
l=0
h=5
print(lomutoPartition(arr,l,h))
print(arr)

