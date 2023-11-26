#In Ist iteration the largest element is bubbled up to last position. 

# def bubbleSort(l):
#     n = len(l)
#     for i in range(n-1):
#         for j in range(n-i-1):  # i is used so that the sorted elements[last] does not get checked as its already sorted 
#             if l[j]>l[j+1]:
#                 l[j], l[j+1] = l[j+1], l[j]


#Optimized way (if list is sorted, it does only one iteration of element)

def bubbleSort(l):
    n = len(l)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):  
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped == False:
            return l
    return l
        
l = [8, 2, 6, 5]
print(bubbleSort(l))

def bubbleSort(self,arr, n):
        for i in range(n-1):
            swapped=False
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped=True
            if swapped==False:
                return arr
            return arr