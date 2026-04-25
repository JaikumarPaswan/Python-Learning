import heapq

A=[-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
heapq.heapify(A)

print(A)



#Heap push insert element
#time: O(log2 n)  #2 denotes base 2

heapq.heappush(A, 4) #This pushes 4 inside the min-heap
print(A)



#Heap pop(extract min)
#Time: O(log2 n)

minn = heapq.heappop(A)
print(A)
print(minn)



#Heap Sort
#Time: O(n log2 n)
#Note: O(1) space is possible via swapping, but this is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn
    
    return new_list

arr = [1, 3, 5, 7, 9, 2, 6, 4, 8, 0]
print(heapsort(arr))



#convert arrray to Max heap
heapq._heapify_max(A)
print(A)

#Heap Push Pop: Time: O(log2 n) #It pushes a element and pops the root of heap
print(A)
heapq.heappushpop(A, 99)
print(A)
