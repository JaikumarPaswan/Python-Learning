#3. First and Last Occurrence of an Element
#Given a sorted array and a target value, find the first and last index of the target. If not found, return -1-1.

#⭐We can also use binary search as array is sorted 

arr=[1,2,2,2,4,5,7,7,9]
target = 2

first = -1
last = -1

for i in range(len(arr)):
    if arr[i]==target:
        first,last=i,i
        break
    
for j in range(i+1, len(arr)):  #[we can use range(first+1, len(arr)) also]
    if arr[j]==target:
        last=j
        

print(first, last)