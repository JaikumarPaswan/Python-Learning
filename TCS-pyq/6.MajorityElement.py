#4. Majority Element
#Given an array of size N, find the element that appears more than N/2 times. If no such element exists, return -1.

arr = [1,2,3,2,3,1,1,4,1]

map={}

for x in arr:
    if x in map:
        map[x]+=1
    else:
        map[x]=1


candidate = max(map, key=map.get)

if map[candidate] > len(arr)//2:
    print(candidate)
else:
    print(-1)

